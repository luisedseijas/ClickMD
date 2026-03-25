# ClickMD: Simulación Molecular para Todos

<div align="center">

**Un MVP de simulación molecular con interfaz gráfica intuitiva para científicos sin experiencia de programación**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

## 🎯 Visión

ClickMD resuelve la **brecha tecnológica** que impide a biólogos experimentales y químicos sintéticos acceder a herramientas modernas de simulación molecular. Aunque son expertos en su dominio, la falta de habilidades de programación los deja fuera.

**ClickMD es la solución:** integra potentes motores de simulación bajo una interfaz gráfica simple, permitiendo a científicos sin conocimientos de programación:

- 📁 Cargar moléculas en segundos
- ⚙️ Seleccionar potenciales (NN o Clásicos)
- ▶️ Ejecutar simulaciones con un clic
- 📊 Ver resultados en tiempo real

## 🏗️ Arquitectura

```
┌─────────────────────────────────────┐
│        GUI (PySide6/Qt)             │  Usuario
│  - Carga de moléculas               │
│  - Visualización 3D                 │
│  - Parámetros de simulación         │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Core de Simulación                 │
│  - Orquestador de tareas            │
│  - Gestor de trabajos               │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
┌─────▼─────┐    ┌──────▼─────┐
│  OpenMM   │    │  TorchANI   │
│Potenciales│    │Potenciales  │
│Clásicos   │    │     NN      │
└───────────┘    └─────────────┘
      │                 │
      └────────┬────────┘
             ↓
     ┌─────────────────┐
     │      ASE        │
     │Manejo químico   │
     └─────────────────┘
```

## 💡 Principios de Diseño

### Prioridad #1: Estabilidad Over Funcionalidad
- Es mejor hacer *una sola cosa perfectamente* que intentar hacer todo y fallar
- MVP inicial: **Simular una molécula pequeña en vacío**
- Mejor 50 usuarios felices que 1000 usuarios frustrados

### Prioridad #2: No Reinventar la Rueda
- **ASE**: gestión química y I/O
- **OpenMM**: simulaciones de alto rendimiento
- **TorchANI**: potenciales de redes neuronales
- **PySide6**: interfaz moderna y profesional

### Prioridad #3: UX para Científicos, no Programadores
- Interfaz intuitiva: un flujo de trabajo claro
- Valores sensatos por defecto
- Mensajes de error claros y orientados a soluciones
- Documentación en español

## 🚀 Características del MVP v0.1

### ✅ Funcionalidades Mínimas
- [ ] Cargar molécula desde archivo (SDF, PDB, MOL2)
- [ ] Seleccionar potencial
  - [ ] Clásico (OpenMM - GAFF, Amber)
  - [ ] Neural Network (TorchANI)
- [ ] Configurar simulación
  - [ ] Temperatura
  - [ ] Duración (pasos o tiempo)
  - [ ] Frecuencia de salida
- [ ] Ejecutar simulación
- [ ] Visualizar trayectoria
- [ ] Exportar resultados (PDB, XTC, CSV)

### ❌ Fuera del Alcance v0.1
- Moléculas en soluciones explícitas (por ahora)
- Cálculos de free energy
- Ensambles Gibbs/NPT
- Solventes implícitos complejos
- Visualizador 3D personalizado (usar VMD/PyMol)

## 📋 Requisitos

### Sistema
- **OS**: macOS 10.14+, Linux, Windows 10+
- **Python**: 3.8 - 3.11
- **RAM**: Mínimo 4GB (8GB+ recomendado)
- **GPU**: Opcional (mejora rendimiento)

### Software
- Conda (recomendado) o pip
- Git (para desarrollo)

## 🔧 Instalación

### 1. Clonar repositorio
```bash
git clone https://github.com/tuusuario/ClickMD.git
cd ClickMD
```

### 2. Crear entorno conda
```bash
conda env create -f environment.yml
conda activate clickmd
```

### 3. Instalar ClickMD en modo desarrollo
```bash
pip install -e ".[dev]"
```

## ▶️ Uso

### Ejecutar la aplicación
```bash
python -m clickmd.main
```

O directamente:
```bash
clickmd
```

### CLI (desarrollo)
```bash
# Simular molécula desde línea de comandos
python -m clickmd.cli --molecule methane.sdf --potential torchani --temperature 298 --time 1000000
```

## 🧪 Pruebas

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=clickmd --cov-report=html

# Test específico
pytest tests/test_simulation.py::test_openmm_basic
```

## 📁 Estructura del Proyecto

```
ClickMD/
├── clickmd/
│   ├── __init__.py              # Metadata del paquete
│   ├── main.py                  # Punto de entrada - GUI principal
│   ├── cli.py                   # Interfaz de línea de comandos
│   │
│   ├── core/                    # Lógica de simulación
│   │   ├── __init__.py
│   │   ├── simulation.py        # Orquestador principal
│   │   ├── openmm_engine.py     # Backend OpenMM
│   │   ├── torchani_engine.py   # Backend TorchANI
│   │   └── molecule.py          # Clase Molecule wrapper
│   │
│   ├── gui/                     # Interfaz gráfica (PySide6)
│   │   ├── __init__.py
│   │   ├── main_window.py       # Ventana principal
│   │   ├── dialogs.py           # Diálogos (abrir, settings, etc)
│   │   ├── widgets.py           # Widgets reutilizables
│   │   ├── visualizer.py        # Visor 3D básico
│   │   └── styles.py            # Estilos y temas
│   │
│   └── utils/                   # Utilidades
│       ├── __init__.py
│       ├── io.py                # Lectura/escritura de moléculas
│       ├── logging.py           # Sistema de logging
│       ├── constants.py         # Constantes (eV, kcal/mol, etc)
│       └── validators.py        # Validación de entrada
│
├── tests/                       # Suite de tests
│   ├── __init__.py
│   ├── conftest.py              # Fixtures pytest
│   ├── test_core.py             # Tests de core
│   ├── test_gui.py              # Tests de GUI
│   └── test_integration.py      # Tests de integración
│
├── docs/                        # Documentación
│   ├── INSTALLATION.md          # Guía de instalación
│   ├── USER_GUIDE.md            # Manual de usuario
│   ├── DEVELOPER_GUIDE.md       # Guía para desarrolladores
│   └── API.md                   # Referencia de API
│
├── examples/                    # Ejemplos (moléculas, configs)
│   └── molecules/               # Moléculas de ejemplo (SDF/PDB)
│
├── pyproject.toml              # Configuración moderna
├── environment.yml              # Especificación conda
├── setup.py                     # Build script (si se necesita)
├── MANIFEST.in                  # Incluir archivos en distribución
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore rules
```

## 🏃 Roadmap

### Fase 1 (v0.1): MVP - En Progreso
- [x] Diseño arquitectónico
- [ ] Backend de simulación (OpenMM + TorchANI)
- [ ] GUI básica (ventana principal, carga de moléculas)
- [ ] Visualización 3D simple
- [ ] Export de resultados

### Fase 2 (v0.2): Robustez
- [ ] Manejo de errores exhaustivo
- [ ] Testing comprehensive
- [ ] Optimización de rendimiento
- [ ] Documentación completa
- [ ] Instalador (PyInstaller)

### Fase 3 (v0.3): Expansión Controlada
- [ ] Múltiples ensambles (NVT, NPT)
- [ ] Análisis de trayectorias
- [ ] Guías de usuario
- [ ] Plugin system

### Fase 4 (v1.0): Release Público
- [ ] Ejecutables para macOS/Windows/Linux
- [ ] Comunidad y feedback users
- [ ] Landing page y documentación web

## 🤝 Contribución

El proyecto está actualmente en fase de desarrollo. Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

### Código de Conducta
- Sé respetuoso com otros contribuidores
- Enfócate en el MVPprimero, expansión después
- Prueba tu código (mínimo 80% cobertura)

## 📚 Documentación

- [Guía de Instalación](docs/INSTALLATION.md)
- [Manual de Usuario](docs/USER_GUIDE.md)
- [Guía de Desarrollo](docs/DEVELOPER_GUIDE.md)
- [Referencia de API](docs/API.md)

## 🛠️ Tecnologías

| Componente | Tecnología | Razón |
|-----------|-----------|-------|
| Simulación clásica | OpenMM | Alto rendimiento, flexible, activamente mantenido |
| Potenciales NN | TorchANI | Precisión DFT, entrenado, fácil de usar |
| Gestión química | ASE | Entrada/salida confiable, estable |
| GUI | PySide6 | Qt moderno, profesional, multiplataforma |
| Testing | pytest | Estándar in facto en Python |
| Documentación | Sphinx | Estándar en proyectos científicos |

## 📊 Benchmarking (Objetivos)

Para versión v0.1:
- Simular metano en vacío: **< 5 segundos**
- Cargar molécula simple (< 100 átomos): **< 2 segundos**
- GUI responsiva durante simulación: **Sí**

## 🐛 Reporte de Bugs

Usa [Issues](https://github.com/tuusuario/ClickMD/issues) de GitHub:
1. Checa si el bug ya fue reportado
2. Proporciona pasos para reproducir
3. Incluye versión Python, OS, stack trace
4. Sugiere fix si es posible

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles

## 👤 Autor

**Luis Seijas**
- GitHub: [@tuusuario](https://github.com/tuusuario)
- Email: tu.email@example.com

---

**Last Updated**: Marzo 2026
**Status**: En Desarrollo 🚧
