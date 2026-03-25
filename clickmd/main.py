#!/usr/bin/env python3
"""
Punto de entrada principal de ClickMD
======================================

Inicia la aplicación PySide6 o la interfaz de línea de comandos
según los argumentos pasados.

Uso:
    python -m clickmd.main           # Inicia GUI
    python -m clickmd.main --help    # Muestra ayuda
"""

import sys
import logging
from pathlib import Path

# Configurar logging básico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_app():
    """
    Inicia la aplicación PySide6.
    
    Este es el punto de entrada principal cuando se ejecuta:
        python -m clickmd.main
        o
        clickmd  (si está instalado)
    """
    logger.info("Iniciando ClickMD...")
    
    try:
        from PySide6.QtWidgets import QApplication
        from clickmd.gui.main_window import MainWindow
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        
        logger.info("ClickMD iniciado correctamente")
        sys.exit(app.exec())
        
    except ImportError as e:
        logger.error(f"Error al importar dependencias: {e}")
        logger.error("Asegúrate de instalar las dependencias: pip install -e .[dev]")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Error fatal al iniciar la aplicación: {e}")
        sys.exit(1)


def run_cli():
    """
    Inicia una interfaz de línea de comandos para simulaciones.
    
    Uso:
        python -m clickmd.main --molecule methane.sdf --potential torchani
    """
    import argparse
    from clickmd.cli import execute_simulation
    
    parser = argparse.ArgumentParser(
        description="ClickMD - Simulación Molecular para Científicos"
    )
    parser.add_argument("--molecule", type=str, required=True,
                       help="Archivo de molécula (SDF, PDB, MOL2)")
    parser.add_argument("--potential", type=str, default="torchani",
                       choices=["torchani", "gaff", "amber"],
                       help="Potencial a usar (default: torchani)")
    parser.add_argument("--temperature", type=float, default=298.15,
                       help="Temperatura en K (default: 298.15)")
    parser.add_argument("--time", type=float, default=1e5,
                       help="Duración en pasos (default: 1e5)")
    parser.add_argument("--output", type=str, default=None,
                       help="Archivo de salida (default: traj.pdb)")
    parser.add_argument("--verbose", action="store_true",
                       help="Modo verbose (más output)")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        execute_simulation(
            molecule_file=args.molecule,
            potential=args.potential,
            temperature=args.temperature,
            time=args.time,
            output_file=args.output
        )
    except Exception as e:
        logger.error(f"Error en simulación: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Detectar si se solicita CLI o GUI
    if len(sys.argv) > 1 and sys.argv[1] in ["--molecule", "-m"]:
        run_cli()
    else:
        run_app()
