"""
Core del módulo de simulación - Orquestador principal
=====================================================

Define la lógica central de simulación, integrando:
- Gestión de moléculas (ASE)
- Motors de simulación (OpenMM, TorchANI)
- Manejo de trabajos y trayectorias
"""

__all__ = [
    "Molecule",
    "SimulationEngine",
    "OpenMMEngine",
    "TorchANIEngine",
]
