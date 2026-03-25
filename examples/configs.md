# Configuraciones de Ejemplo

## config_basic.json

```json
{
  "molecule_file": "examples/molecules/methane.pdb",
  "potential": "torchani",
  "temperature": 298.15,
  "n_steps": 100000,
  "timestep": 1,
  "output_file": "traj_methane.pdb",
  "save_frequency": 100
}
```

## config_advanced.json

```json
{
  "molecule_file": "examples/molecules/alanine.pdb",
  "potential": "amber",
  "temperature": 310.15,
  "n_steps": 500000,
  "timestep": 1,
  "output_file": "traj_alanine.pdb",
  "save_frequency": 50,
  "integrator": "langevin",
  "friction": 0.01
}
```

## Usage

```bash
python -m clickmd.cli --config config_basic.json
```
