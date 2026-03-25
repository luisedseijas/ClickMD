"""
Tests del core de simulación
=============================

Tests para los motores de simulación:
- OpenMMEngine
- TorchANIEngine
- Molecule
"""

import pytest


class TestMolecule:
    """Tests para la clase Molecule."""
    
    def test_load_molecule(self):
        """Test cargar una molécula."""
        pytest.skip("No implementado aún")
    
    def test_get_atoms(self):
        """Test obtener átomos de molécula."""
        pytest.skip("No implementado aún")


class TestOpenMMEngine:
    """Tests para el motor OpenMM."""
    
    def test_initialize_engine(self):
        """Test inicializar motor OpenMM."""
        pytest.skip("No implementado aún")
    
    def test_run_simulation(self):
        """Test ejecutar simulación básica."""
        pytest.skip("No implementado aún")


class TestTorchANIEngine:
    """Tests para el motor TorchANI."""
    
    def test_initialize_engine(self):
        """Test inicializar motor TorchANI."""
        pytest.skip("No implementado aún")
    
    def test_run_simulation(self):
        """Test ejecutar simulación con NN."""
        pytest.skip("No implementado aún")
