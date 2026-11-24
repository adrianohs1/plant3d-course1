# 01 — Project Setup, Grids & Structural Steel

## Project & Workspace Setup

- **Project types:** a Plant 3D project holds both `P&ID PIP` (2D P&ID drawings) and `3D Piping` (model drawings). Keep them distinct in the Project Manager.
- **Drawing properties:** set drawing properties on creation (project, area, description) so reports pick them up.
- **Units:** `mm` throughout (drawing units, nozzle sizes, elevations).

## Grids & Structural Steel

### Structure tab

- Use the **Structure** tab to create grids and steel.
- **Model type:**
  - `Line Model` — lightweight centrelines, quick to edit.
  - `Shape Model` — full section geometry; use for final steel and clash checks.

### Grid example

| Parameter | Value |
|-----------|-------|
| Axis      | `0, 9000` |
| Row       | `0, 12000` |
| Platform  | `0, 5000, 10000` |

- Stair offsets: `1000 mm`.
- Use `EXPLODE` **only** to remove unwanted grid lines — not for general editing.

### Steel editing

- `Edit Structure` — align members to **top of steel**.
- Trim, mitre and cut-back members where they meet.
- Turn off the `GRID` layer before plotting/ortho creation.

### Stairs

| Parameter | Value |
|-----------|-------|
| Width | `800` |
| Max tread | `250` |
| Stringer | `U-200` |

### Ladders

| Parameter | Value |
|-----------|-------|
| Cage | on |
| Stand-off | `200` |
| Start height | `2800` |
| Max distance | `1500` |

### Other structural items

- **Grating openings:** cut openings where pipes pass through platforms.
- **Handrail gaps:** leave gaps at stair/ladder access points.
- **Footings:** add under columns at grade.
