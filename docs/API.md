# Referencia de API - ClickMD

## Módulo: clickmd.core

### Clase: Molecule

Envoltorio para moléculas con manejo de entrada/salida.

```python
class Molecule:
    def __init__(self, ase_atoms: ase.Atoms)
    def from_file(cls, filepath: str) -> Molecule
    def save(self, filepath: str)
    
    @property
    def atoms(self) -> ase.Atoms
    @property
    def n_atoms(self) -> int
    @property
    def positions(self) -> np.ndarray
    @property
    def symbols(self) -> List[str]
    @property
    def masses(self) -> np.ndarray
```

### Clase: SimulationEngine (ABC)

Interfaz base para motores de simulación.

```python
class SimulationEngine(ABC):
    @abstractmethod
    def initialize(self, molecule: Molecule, temperature: float)
    @abstractmethod
    def run(self, n_steps: int) -> Trajectory
    @abstractmethod
    def get_energy(self) -> float
    @abstractmethod
    def get_forces(self) -> np.ndarray
```

### Clase: OpenMMEngine

Motor de simulación clásica basado en OpenMM.

```python
class OpenMMEngine(SimulationEngine):
    def __init__(self, forcefield: str = "amber")
    def initialize(self, molecule: Molecule, temperature: float)
    def run(self, n_steps: int) -> Trajectory
    def get_energy(self) -> float
    def get_forces(self) -> np.ndarray
```

**Parámetros de forcefield**:
- `"amber"` - AMBER force field
- `"gaff"` - General AMBER force field
- `"charmm"` - CHARMM force field (si está disponible)

### Clase: TorchANIEngine

Motor de simulación con redes neuronales (TorchANI).

```python
class TorchANIEngine(SimulationEngine):
    def __init__(self, model: str = "ani2x")
    def initialize(self, molecule: Molecule, temperature: float)
    def run(self, n_steps: int) -> Trajectory
    def get_energy(self) -> float
    def get_forces(self) -> np.ndarray
```

**Modelos disponibles**:
- `"ani2x"` - Modelo trained en ANAKIN-ME
- `"ani2ens"` - Ensemble de modelos (más lento, más preciso)

---

## Módulo: clickmd.utils

### Función: load_molecule

```python
def load_molecule(filepath: str) -> Molecule:
    """Cargar molécula desde archivo."""
```

**Formatos soportados**: PDB, SDF, MOL2

### Función: save_trajectory

```python
def save_trajectory(trajectory: Trajectory, filepath: str)
    """Guardar trayectoria a archivo."""
```

**Formatos soportados**: PDB, XTC, DCD, H5

### Constantes

```python
# Conversiones de energía
EV_TO_KCAL_MOL = 23.061
KCAL_MOL_TO_EV = 1 / EV_TO_KCAL_MOL
KCAL_MOL_TO_KJ_MOL = 4.184

# Temperatura
ROOM_TEMPERATURE = 298.15  # K
BODY_TEMPERATURE = 310.15  # K (37°C)

# Físicas
BOLTZMANN = 8.314e-3  # kJ/(mol·K)
AVOGADRO = 6.022e23
```

---

## Módulo: clickmd.gui

### Clase: MainWindow

Ventana principal de la aplicación.

```python
class MainWindow(QMainWindow):
    def __init__(self)
    def load_molecule(self)
    def run_simulation(self)
    
    # Signals
    simulation_started = pyqtSignal()
    simulation_finished = pyqtSignal(Trajectory)
    simulation_error = pyqtSignal(str)
```

### Clase: MoleculeVisualizer

Visualizador 3D de moléculas (placeholder para v0.1).

```python
class MoleculeVisualizer(QWidget):
    def __init__(self)
    def set_molecule(self, molecule: Molecule)
    def update_positions(self, positions: np.ndarray)
```

---

## Ejemplos de Uso

### Ejemplo 1: Simulación Simple

```python
from clickmd.core import Molecule, OpenMMEngine

# Cargar molécula
mol = Molecule.from_file("methane.pdb")

# Crear y ejecutar simulación
engine = OpenMMEngine()
engine.initialize(mol, temperature=298.15)
trajectory = engine.run(n_steps=100000)

# Guardar resultados
trajectory.save("results.pdb")
```

### Ejemplo 2: Con TorchANI

```python
from clickmd.core import Molecule, TorchANIEngine

mol = Molecule.from_file("ethane.sdf")
engine = TorchANIEngine(model="ani2x")
engine.initialize(mol, temperature=300)
traj = engine.run(n_steps=50000)
```

### Ejemplo 3: Desde CLI

```bash
clickmd --molecule drug.sdf --potential torchani --temperature 310 --time 500000
```

---

## Tipo de Datos: Trajectory

Representa una trayectoria de simulación.

```python
class Trajectory:
    @property
    def n_frames(self) -> int
    @property
    def n_atoms(self) -> int
    @property
    def frames(self) -> List[np.ndarray]
    
    def get_frame(self, idx: int) -> np.ndarray
    def save(self, filepath: str)
    def get_energies(self) -> np.ndarray
```

---

## Excepciones Personalizadas

```python
class ClickMDError(Exception):
    """Error base de ClickMD."""

class MoleculeError(ClickMDError):
    """Error al cargar/procesar molécula."""

class SimulationError(ClickMDError):
    """Error durante simulación."""

class UnsupportedFormatError(ClickMDError):
    """Formato de archivo no soportado."""
```

---

## Configuración

Ver `clickmd/config.py` para valores por defecto y constantes.

```python
# Default values
DEFAULT_TEMPERATURE = 298.15  # K
DEFAULT_STEPS = 100000
DEFAULT_FORCEFIELD = "amber"
DEFAULT_TIMESTEP = 1  # femtosegundos

# UI
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
```

---

**Last Updated**: Marzo 2026
