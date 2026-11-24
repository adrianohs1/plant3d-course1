# 02 — Specs, Parametric Components & Data Manager / MTO

## Specs & Parametric Components

### Connection types

| Code | Meaning |
|------|---------|
| `FL` | Flanged |
| `BW` | Butt weld |
| `SW` | Socket weld |
| `THD` | Threaded |

### Flange standards & ratings

- `PN10` — pressure nominal 10 bar.
- `DIN 2632` — PN10 flange standard (used for course nozzles).
- `150# RF` — ASME Class 150, raised face.

### Branches

- Branch types come from the spec's branch table (tee, reducing tee, olet, stub-in). Check the table when a branch is not offered.

### Substitute Part

- Select a placed part and use its **grips** to run `Substitute Part`, swapping for another catalog part of the same size/spec without re-routing.

### Nozzle checks

- Units: `mm`.
- Connection: `FL`.
- Pressure Class: `10`.
- Standard: `DIN 2632`.

## Data Manager & MTO

### Opening Data Manager

- `Home` tab → **Data Manager**.
- Data sets available:
  - `P&ID Project Data`
  - `Plant 3D Project Data`
  - `Project Reports`

### Excel export

- Export to Excel from Data Manager.
- Options: `Displayed data` and `Active node only`.
- Add **name and student number** to the exported sheet as required by the assignment.

### MTO accuracy stages

| Stage | Accuracy |
|-------|----------|
| Order of magnitude (OOM) | `±30–50%` |
| Bulk MTO | `±30%` → `±10%` |
| Detailed MTO | From the 3D model / isometrics |
