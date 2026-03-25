"""
Configuración de pytest
=======================

Define fixtures y configuración compartida para todos los tests.
"""

import pytest


@pytest.fixture
def example_molecule():
    """Fixture que proporciona una molécula de prueba."""
    # TODO: Cargar una molécula de ejemplo pequeña
    pass
