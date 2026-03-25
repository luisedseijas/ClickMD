"""
ClickMD: Simulación Molecular para Científicos sin Experiencia de Programación
==============================================================================

Una solución MVP que integra OpenMM + TorchANI bajo una interfaz gráfica
intuitiva (PySide6), permitiendo a biólogos y químicos acceder a herramientas
modernas de simulación molecular sin necesidad de código.

Visión:
  Resolver la brecha tecnológica que impide a científicos experimentales
  acceder a hetramientas de simulación de vanguardia.

Estrategia:
  - Prioridad #1: Estabilidad sobre funcionalidad
  - Prioridad #2: No reinventar la rueda (ASE, OpenMM, TorchANI)
  - Prioridad #3: UX intuitiva para científicos

Uso:
  from clickmd import run_app
  run_app()
  
  o desde CLI:
  $ python -m clickmd.main
"""

__version__ = "0.1.0"
__author__ = "Luis Seijas"
__license__ = "MIT"

# Versiones de dependencias críticas requeridas
__requires_openmm__ = ">=8.0"
__requires_torchani__ = ">=2.2"
__requires_pyside6__ = ">=6.5"
__requires_ase__ = ">=3.23"

from .main import run_app

__all__ = ["run_app", "__version__"]
