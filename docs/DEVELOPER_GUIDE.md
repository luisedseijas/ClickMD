# Guía para Desarrolladores - ClickMD

## Arquitectura del Proyecto

```
ClickMD/
├── clickmd/
│   ├── main.py              # Punto de entrada
│   ├── cli.py               # Interfaz CLI
│   │
│   ├── core/                # Lógica de simulación
│   │   ├── simulation.py     # Orquestador
│   │   ├── openmm_engine.py  # Backend OpenMM
│   │   ├── torchani_engine.py# Backend TorchANI
│   │   └── molecule.py       # Gestión de moléculas
│   │
│   ├── gui/                 # Interfaz gráfica
│   │   ├── main_window.py    # Ventana principal
│   │   ├── dialogs.py        # Diálogos
│   │   └── visualizer.py     # Visualización 3D
│   │
│   └── utils/               # Funciones de soporte
│       ├── io.py            # I/O de moléculas
│       ├── logging.py        # Sistema de logging
│       ├── constants.py      # Constantes químicas
│       └── validators.py     # Validación
│
├── tests/                   # Suite de tests
│   ├── test_core.py
│   ├── test_gui.py
│   └── test_integration.py
│
└── docs/                    # Documentación
    ├── INSTALLATION.md
    ├── USER_GUIDE.md
    ├── DEVELOPER_GUIDE.md
    └── API.md
```

## Configuración del Entorno de Desarrollo

### 1. Clonar y Configurar

```bash
git clone https://github.com/tuusuario/ClickMD.git
cd ClickMD
conda env create -f environment.yml
conda activate clickmd
pip install -e ".[dev]"
```

### 2. Verificar Setup

```bash
# Tests
pytest

# Linting
black --check clickmd/
flake8 clickmd/
isort --check clickmd/
```

## Estándares de Código

### Python Style
- **Formato**: Black (línea 100 caracteres)
- **Imports**: isort (profiles=black)
- **Linting**: flake8
- **Type hints**: Recomendado (no obligatorio)

### Formateo Automático

```bash
# Auto-format
black clickmd/
isort clickmd/

# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
black clickmd/ tests/
isort clickmd/ tests/
EOF
chmod +x .git/hooks/pre-commit
```

### Documentación

Usa docstrings en formato Google:

```python
def load_molecule(file_path: str) -> Molecule:
    """
    Carga una molécula desde archivo.
    
    Args:
        file_path: Ruta al archivo (PDB, SDF, MOL2)
        
    Returns:
        Objeto Molecule cargado
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato no es soportado
        
    Example:
        >>> mol = load_molecule("methane.pdb")
        >>> mol.n_atoms
        5
    """
```

## Estructura de Datos Principal

### Clase Molecule

```python
class Molecule:
    """Envoltorio para moléculas ASE."""
    
    def __init__(self, ase_atoms):
        self.atoms = ase_atoms  # ASE Atoms object
        
    @property
    def n_atoms(self) -> int:
        """Número de átomos."""
        
    @property
    def positions(self) -> np.ndarray:
        """Posiciones en Ångstroms."""
        
    def save(self, filename: str):
        """Guardar a archivo."""
```

### Clase SimulationEngine (ABC)

```python
class SimulationEngine(ABC):
    """Clase base para motores de simulación."""
    
    @abstractmethod
    def initialize(self, molecule: Molecule, temp: float):
        """Inicializar simulación."""
        
    @abstractmethod
    def run(self, n_steps: int) -> Trajectory:
        """Ejecutar simulación."""
        
    @abstractmethod
    def get_energy(self) -> float:
        """Obtener energía actual."""
```

## Workflow de Desarrollo

### 1. Crear Feature Branch

```bash
git checkout -b feature/mi-caracteristica
```

### 2. Hacer Cambios

```bash
# Editar código
vim clickmd/core/simulation.py

# Escribir tests
vim tests/test_core.py

# Probar
pytest tests/test_core.py -v
```

### 3. Commit

```bash
git add clickmd/ tests/
git commit -m "feat: agregar soporte para X

- Implementar clase X
- Agregar tests para X
- Actualizar documentación"
```

Mensajes de commit:
- `feat:` - Nueva característica
- `fix:` - Bug fix
- `docs:` - Documentación
- `test:` - Tests
- `refactor:` - Refactorización

### 4. Push y Pull Request

```bash
git push origin feature/mi-caracteristica
# Abre PR en GitHub
```

## Testing

### Ejecutar Tests

```bash
# Todos
pytest

# Con cobertura
pytest --cov=clickmd --cov-report=html

# Un archivo
pytest tests/test_core.py

# Una función
pytest tests/test_core.py::TestMolecule::test_load_molecule -v

# Con output
pytest -s tests/test_core.py
```

### Escribir Tests

```python
import pytest
from clickmd.core import Molecule

class TestMolecule:
    
    @pytest.fixture
    def example_mol(self):
        """Fixture para molécula de prueba."""
        return load_molecule("test.pdb")
    
    def test_load_molecule(self, example_mol):
        """Test cargar molécula."""
        assert example_mol.n_atoms > 0
    
    def test_invalid_file(self):
        """Test error con archivo inválido."""
        with pytest.raises(FileNotFoundError):
            load_molecule("noexiste.pdb")
```

## Debugging

### Logging

```python
import logging
logger = logging.getLogger(__name__)

logger.debug("Información de debug")
logger.info("Información general")
logger.warning("Advertencia")
logger.error("Error")
logger.critical("Error crítico")
```

### En Desarrollo

```python
# En main.py
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run_app()
```

### Debugger (pdb)

```python
import pdb; pdb.set_trace()  # Pausa aquí
```

## Workflow de Simulación

```python
# 1. Cargar molécula
from clickmd.core import Molecule
mol = Molecule.from_file("methane.pdb")

# 2. Crear engine
from clickmd.core import OpenMMEngine
engine = OpenMMEngine()

# 3. Inicializar
engine.initialize(mol, temperature=298.15)

# 4. Ejecutar
traj = engine.run(n_steps=100000)

# 5. Analizar
print(f"Energía final: {engine.get_energy()} eV")
traj.save("trajectory.pdb")
```

## Agregar Nueva Característica

### Ejemplo: Agregar soporte para nuevo potencial

1. **Crear engine**
   ```python
   # clickmd/core/mydescriptor_engine.py
   from clickmd.core import SimulationEngine
   
   class MyDescriptorEngine(SimulationEngine):
       def initialize(self, mol, temp):
           pass
       
       def run(self, n_steps):
           pass
   ```

2. **Escribir tests**
   ```python
   # tests/test_mydescriptor.py
   def test_mydescriptor_engine():
       engine = MyDescriptorEngine()
       # ...
   ```

3. **Registrar en GUI**
   ```python
   # clickmd/gui/main_window.py
   self.potential_combo.addItem("MyDescriptor")
   ```

4. **Documentar**
   - Actualizar README
   - Agregar docstring
   - Ejemplos en docs/

## Compilar Ejecutable

### Con PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile --windowed clickmd/main.py --name ClickMD
```

El ejecutable estará en `dist/`

## Próximos Pasos

- Lee [API.md](API.md) para referencia completa
- Explora `clickmd/` para entender la arquitectura
- Revisa [Issues Abiertos](https://github.com/tuusuario/ClickMD/issues) para tareas

---

**Last Updated**: Marzo 2026
