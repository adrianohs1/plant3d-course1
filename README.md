# plant3d-course

Workspace for **MECH7022 — 3D Piping Design** (AutoCAD Plant 3D, P&ID, 3D Steel, 3D Piping, Orthos, Isos & MTOs).

## Folder & File Rules

- **Keep large, binary and live CAD files out of Git.**
  - Live Plant 3D projects: `*.dwg`, `*.dcf`, `*.pspx`, `*.pspc`, `*.pcat`, `Project.xml`.
  - Exports: `*.pdf`, raw `*.xlsx` dumps, plots, screenshots.
  - Reference books and slides.
  - These stay in `cad-local/`, `exports/`, or Google Drive.
- **Track human-readable knowledge and code in Git.**
  - Markdown notes and spec summaries.
  - Clean CSV schedules (e.g. `bom.csv`).
  - Scripts (`*.py`, `*.lsp`).
  - Drive link indexes.
- **Git safety:** never commit or push without explicit confirmation.

## Naming & Engineering Conventions (MECH7022)

- **Line tags:** `Size-Spec-Service-Number`
  - e.g. `150-10HS01-BFWS-1001`, `100-10HS01-PW-1001`.
- **Equipment tags:** `F-101`, `F-102`, `P-301`, `P-302`, `E-101`, `E-102`, `TK-101`
  - Verify no `?` placeholders remain.
- **Nozzle rules (A2 / 3D):**
  - Units in `mm`.
  - Flanged (`FL`), `DIN 2632`, `PN10` / Pressure Class `10` where required by spec/brief.
- **Elevations & routing:**
  - Keep piping grouped along walls/structures.
  - Avoid low-level floor trip hazards across walkways.
  - Maintain `>= 2200 mm` BOP over walkways (`2100 mm` clearance + `100 mm` support allowance).
  - Use thermal expansion offsets (`Z`-bends / expansion loops) where appropriate.
- **Project naming:** follow assignment instructions (e.g. `A1 Surname Firstname`, `A2`, `A3 Surname First Name`).

## Layout

```
plant3d-course/
├── README.md
├── .gitignore
├── notes/                      # course notes (tracked)
├── projects/
│   └── lab-01-skid-piping/
│       ├── spec-summary.md     # tracked
│       ├── bom.csv             # tracked (clean schedule)
│       ├── exports/            # ignored
│       └── cad-local/          # ignored (live CAD)
├── scripts/
│   ├── lisp/layer_check.lsp
│   └── python/bom_summary.py
└── reference/drive-links.md
```
