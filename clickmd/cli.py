#!/usr/bin/env python3
"""
Interfaz de línea de comandos (CLI)
====================================

Permite ejecutar simulaciones desde la terminal sin usar la GUI.

Uso:
    python -m clickmd.cli --molecule methane.sdf --potential torchani --temperature 298 --time 100000
"""

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def execute_simulation(
    molecule_file: str,
    potential: str = "torchani",
    temperature: float = 298.15,
    time: float = 1e5,
    output_file: Optional[str] = None,
) -> bool:
    """
    Ejecuta una simulación desde CLI.
    
    Args:
        molecule_file: Ruta al archivo de molécula
        potential: Potencial a usar ("torchani", "gaff", "amber")
        temperature: Temperatura en Kelvin
        time: Duración de simulación en pasos
        output_file: Archivo de salida (default: traj.pdb)
        
    Returns:
        True si la simulación fue exitosa, False de lo contrario
    """
    try:
        # Validar entrada
        mol_path = Path(molecule_file)
        if not mol_path.exists():
            logger.error(f"Archivo no encontrado: {molecule_file}")
            return False
            
        if potential not in ["torchani", "gaff", "amber"]:
            logger.error(f"Potencial desconocido: {potential}")
            return False
            
        if temperature < 0 or temperature > 10000:
            logger.error(f"Temperatura fuera de rango: {temperature} K")
            return False
        
        logger.info(f"Iniciando simulación...")
        logger.info(f"  Molécula: {molecule_file}")
        logger.info(f"  Potencial: {potential}")
        logger.info(f"  Temperatura: {temperature} K")
        logger.info(f"  Duración: {time} pasos")
        
        # TODO: Implementar lógica de simulación
        logger.warning("CLI aún no implementada - característica en desarrollo")
        
        return True
        
    except Exception as e:
        logger.error(f"Error en simulación: {e}")
        return False


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="ClickMD CLI")
    parser.add_argument("--molecule", type=str, required=True)
    parser.add_argument("--potential", type=str, default="torchani")
    parser.add_argument("--temperature", type=float, default=298.15)
    parser.add_argument("--time", type=float, default=1e5)
    parser.add_argument("--output", type=str, default=None)
    
    args = parser.parse_args()
    success = execute_simulation(**vars(args))
    exit(0 if success else 1)
