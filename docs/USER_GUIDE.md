# Manual del Usuario - ClickMD

## Inicio Rápido

1. **Inicia ClickMD**
   ```bash
   clickmd
   ```

2. **Carga una molécula**
   - Click en "Cargar Molécula"
   - Selecciona un archivo (PDB, SDF, MOL2)

3. **Configura la simulación**
   - Selecciona potencial (TorchANI o Clásico)
   - Ajusta temperatura (K)
   - Ajusta duración (pasos)

4. **Ejecuta**
   - Click en "Ejecutar Simulación"
   - Espera a que termine
   - Visualiza resultados

---

## Interfaz Principal

```
┌─────────────────────────────────────────────────────┐
│  ClickMD - Simulación Molecular                    │
├──────────────────────┬──────────────────────────────┤
│ Controles            │ Visualización 3D             │
│                      │                              │
│ ☐ Cargar Molécula    │  [Molécula 3D aquí]          │
│                      │                              │
│ Potencial:           │                              │
│ ▼ TorchANI           │                              │
│                      │                              │
│ Temperatura (K):     │                              │
│ [298.15]             │                              │
│                      │                              │
│ Duración (pasos):    │                              │
│ [100000]             │                              │
│                      │                              │
│ [Ejecutar Simulación]│                              │
│                      │                              │
└──────────────────────┴──────────────────────────────┘
  Estado: Listo
```

---

## Potenciales Disponibles

### TorchANI (Redes Neuronales)
- **Ventajas**: Precisión DFT, rápido, bueno para orgánicos
- **Desventajas**: Solo entrenado en C, H, N, O
- **Mejor para**: Moléculas orgánicas pequeñas
- **Ejemplo**: péptidos, fármacos, moléculas naturales

### GAFF (Generico - Clásico)
- **Ventajas**: Funciona para muchos elementos
- **Desventajas**: Menos preciso que TorchANI
- **Mejor para**: Moléculas con metales, elementos raros
- **Ejemplo**: complejos metálicos, inorgánicos

### Amber (Biomoléculas)
- **Ventajas**: Optimizado para proteínas/ADN
- **Desventajas**: Solo útil para biomoléculas
- **Mejor para**: Proteínas, ácidos nucleicos
- **Ejemplo**: prótidos, ADN, ARN

---

## Formatos de Molécula Soportados

- **PDB** (.pdb) - Estándar para estructuras 3D
- **SDF** (.sdf) - Formato químico portátil
- **MOL2** (.mol2) - Formato de estructura molecular

### Cómo obtener moléculas

1. **PubChem**: https://pubchem.ncbi.nlm.nih.gov/
   - Busca por nombre
   - Descarga en formato SDF o PDB

2. **DrugBank**: https://go.drugbank.com/
   - Base de datos de drogas

3. **Protein Data Bank**: https://www.rcsb.org/
   - Estructuras de proteínas

4. **ChemSpider**: http://www.chemspider.com/
   - Moléculas por SMILES

---

## Parámetros de Simulación

### Temperatura
- **Rango válido**: 0 - 10,000 K
- **Típico**: 298.15 K (25°C) = temperatura ambiente
- **Consejo**: Aumenta para explorar más conformaciones

### Duración
- **Pasos totales**: 1 paso = 1 femtosegundo (fs)
- **Rango**: 100 - 10,000,000 pasos
- **Ejemplos**:
  - 10,000 pasos = 10 picosegundos (ps)
  - 100,000 pasos = 100 ps
  - 1,000,000 pasos = 1 nanosegundo (ns)
- **Consejo**: Empieza con 100,000 para tests rápidos

---

## Interpretación de Resultados

## Exportar Resultados

La trayectoria se guarda automáticamente como `trajectory.pdb`

Para análisis avanzado:
- **VMD**: https://www.ks.uiuc.edu/Research/vmd/
- **PyMol**: https://pymol.org/
- **Gromacs**: https://www.gromacs.org/

---

## FAQs

**P: Mi simulación es muy lenta**
R: Verifica que estés usando GPU. Si usas CPU, reduce la duración o el tamaño molecular.

**P: Recibo error "Potencial no disponible"**
R: Instala las dependencias: `conda install -c conda-forge openmm torchani`

**P: ¿Cómo agrego mi propia molécula?**
R: Convierte a PDB o SDF usando: 
- Avogadro: https://avogadro.cc/
- OpenBabel: http://openbabel.org/
- RDKit: https://www.rdkit.org/

---

## Próximos Pasos

- Lee [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) si quieres contribuir
- Consulta [API.md](API.md) para uso por programación
- Reporta bugs en GitHub

---

**Last Updated**: Marzo 2026
