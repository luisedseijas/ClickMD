# Guía de Instalación - ClickMD

## Requisitos del Sistema

### Hardware Mínimo
- **CPU**: Dual-core (4 cores recomendado)
- **RAM**: 4 GB (8 GB recomendado)
- **Disco**: 5 GB (para dependencias y simulaciones)
- **GPU**: Opcional (CUDA/OpenCL para mejor performance)

### Sistema Operativo
- macOS 10.14+
- Linux (Ubuntu 18.04+, Fedora 30+)
- Windows 10+

### Software Requerido
- Python 3.8 - 3.11
- Conda (recomendado)

---

## Instalación Rápida

### Opción 1: Conda (Recomendado)

```bash
# 1. Clonar repositorio
git clone https://github.com/tuusuario/ClickMD.git
cd ClickMD

# 2. Crear entorno
conda env create -f environment.yml

# 3. Activar entorno
conda activate clickmd

# 4. Instalar en modo desarrollo
pip install -e .

# 5. Ejecutar
clickmd
```

### Opción 2: pip + venv

```bash
# 1. Clonar
git clone https://github.com/tuusuario/ClickMD.git
cd ClickMD

# 2. Crear venv
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar ClickMD
pip install -e .

# 5. Ejecutar
clickmd
```

---

## Instalación Avanzada

### Compilar desde Fuente

```bash
cd ClickMD
python setup.py sdist bdist_wheel
pip install dist/clickmd-0.1.0-py3-none-any.whl
```

### Con GPU (CUDA)

Para usar GPU con OpenMM:

```bash
# En conda:
conda install -c conda-forge openmm-cuda

# O con pip:
pip install openmm-cuda
```

---

## Verificar Instalación

```bash
# Chequear versiones
python -c "from clickmd import __version__; print(__version__)"

# Chequear dependencias
python -c "import openmm; import torchani; import pyside6; print('OK')"

# Ejecutar tests
pytest
```

---

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'openmm'"

```bash
conda activate clickmd
conda install -c conda-forge openmm
```

### Error: "No module named 'PySide6'"

```bash
pip install PySide6>=6.5
```

### ClickMD lento en simulaciones

Asegúrate de usar GPU:
- Instala `openmm-cuda` o `openmm-hip` según tu hardware
- OpenMM automáticamente usará GPU si está disponible

### Problemas en Windows

Algunos usuarios reportan issues con OpenMM en Windows. Solución:

```bash
conda install -c omnia openmm
```

---

## Próximos Pasos

1. Lee [USER_GUIDE.md](USER_GUIDE.md) para aprender a usar ClickMD
2. Explora los [ejemplos](../examples/)
3. Reporta problemas en [Issues](https://github.com/tuusuario/ClickMD/issues)

---

**Last Updated**: Marzo 2026
