"""
Setup para distribución y builds
=================================

Script para crear paquetes y ejecutables.
Usar: python setup.py bdist_wheel
"""

from setuptools import setup, find_packages
from pathlib import Path

# Leer el README
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="clickmd",
    version="0.1.0",
    author="Luis Seijas",
    description="MVP de simulación molecular con GUI para biólogos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/ClickMD",
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "clickmd=clickmd.main:run_app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
