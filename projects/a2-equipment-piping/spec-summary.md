# Assessment 2 — Equipment Piping: Spec Summary

**Status:** DRAFT — merged from the A2 brief requirements checklist (source: `Assessment_2_Mid_Week_9.docx` plus the lecturer's Assessment 2 CHECK LIST). Anything the brief doesn't state is `<TBC>`.

## 1. Project & drawing setup

- Copy of A1 project; folder renamed `A1 A2 Surname Firstname`
- New drawing `TC 3D Layout`; DWG Number `3D 001`; Description `A1 Surname FirstName` (brief says A1 as written — confirm)
- Save with the P3D icon → Save (not Save As); close and reopen to confirm

## 2. Grid

- Origin `0,0,0`; X `0, 9000` (east/west); Y `0, 12000` (north/south); Z `0, 5000, 10000`
- `<TBC>` which end of X is east; that +Y is north (plan view: N up, stairs on the right/east)

## 3. Equipment & layout

| Item | Brief says | `<TBC>` |
|------|------------|---------|
| `F-101`, `F-102` | Plate frame HX used as furnace; cube D 1000, W 1500, H 1500; copy with 1000 gap; one common `150` plinth; south end, side by side | Insertion point, rotation, base height, nozzle face, how the gap is measured |
| `E-101` | Shell & tube, 4 m overall, capped ends, `DN450`, centreline `1200` above floor, against north wall | Position along wall; shell support |
| `P-301`, `P-302` | Centrifugal; `150` plinth; `800` gap between pumps; west side, north of centre, stacked north–south | Coordinates, rotation; whether 800 is baseplate or plinth; datasheet dimensions |
| Main header (LPHW return) | `DN150`, `10HC01`, 4000 long, 300 from side wall, at pump suction level, blank flange both ends | Which side wall; Y start/end; suction level value |

## 4. Nozzles & ratings

| Equipment | Nozzle | Size (mm) | Position | Rating |
|-----------|--------|-----------|----------|--------|
| `F-101`, `F-102` | 2 each | 80 | EL 700 and EL 1200 | `PN10`, `FL`, `DIN 2632` |
| `E-101` | N1 | 100 | 400 from East end | `<TBC>` |
| `E-101` | N2 | 80 | 675 from East end | `<TBC>` |
| `E-101` | N3 | 80 | 675 from West end | `<TBC>` |
| `E-101` | N4 | 100 | 400 from West end | `<TBC>` |
| `P-301`, `P-302` | Suction | 100 | pump | `PN10` flange |
| `P-301`, `P-302` | Discharge | 80 | pump | `PN10` flange |
| Header | Both ends | `DN150` | blind flange | `<TBC>` |

Also `<TBC>`: furnace outlet vs return nozzle; `E-101` nozzle directions and circuits; flange standard for pumps and `E-101`.

## 5. Pipework & valves

| Line | Size / spec | Required |
|------|-------------|----------|
| Furnaces → header | `DN100`, `10HC01` | Butterfly shut-off valve (hand lever) at each furnace exit; flow meter on common line |
| Header → pumps | suction `100` | Each pump fed from header; drain valve before each pump |
| `80` supply | `80` | One end of header; isolating ball valves before and after the 3-way position; exits north wall, west side, `EL 3700`, flange at grid boundary |
| `80` return | `80` | Opposite header end; double-reg valve before bypass intersection; exits north wall, west side, `EL 3700`, flange at grid boundary |
| Bypass (supply → return) | `<TBC>` | Double-reg valve; 3-way valve omitted — simple tee at each end, valves and flanges at tee outlets |
| HX outlet → furnaces | `100`, `PN10` | Double-reg valve to each furnace; isolating butterfly valve at each furnace return |

`<TBC>`: which header end is supply/return; spec of all lines except header and furnace-to-pump pipework; "common line" location; flow meter type/size; valve type at tee outlets; branch spec to pumps.
**Not in the brief:** pump discharge pipework to `E-101` (size, spec, check/isolation valves, nozzle).

## 6. Drains & elevations

| Item | Value |
|------|-------|
| `80` lines exit (north wall, west side) | `EL 3700` |
| Drain to grade | `EL 200` |
| Furnace nozzles | `EL 700` and `EL 1200` |
| `E-101` centreline | `1200` above floor |
| Plinths | `150` |
| Header level | pump suction level — `<TBC>` |

- One common `DN25` drain valve and line from the `80` bypass to grade at `EL 200`
- Drain valve before each pump — `<TBC>` size, type, where it drains

## 7. Steel

- Platform "as per grid elevations" with stairs and ladder; plan labels LVL 0 and LVL 1 & 2 → platforms at `5000` and `10000` (inferred, `<TBC>`)
- Stairs: east side, running north–south (LVL 1 & 2 plan shows them toward the north-east)
- Ladder: outside the footprint, on the **west wall toward the south end — not at the corner** (brief)
- `<TBC>`: platform extent, member sizes, plate/grating, stair width/tread/rise, ladder cage and level served, footings

## 8. Headroom & routing

- Brief gives no headroom, clearance, slope or support-spacing values (`<TBC>`)
- Brief routing rules: `80` lines exit north wall west side at `EL 3700` with flanges at grid boundary; header 300 from side wall at pump suction level
- Check list: head heights, trip hazards, piping grouped together, supports, drains, extra valves if required
- **Course guidance (not in brief):** Week 7 tutorial — `2100` minimum clearance, `2200` BOP over a beam (this repo's README uses `>= 2200 mm` BOP over walkways)

## 9. Tagging

- Stated: `F-101`, `F-102`, `P-301`, `P-302`
- Check list requires line numbers and equipment tags
- `<TBC>`: `E-101` tag (A1 P&ID uses `E-101`), valve tags (`HA-1xx`), line number format (lecturer's sample uses `Size-Spec-Service-Number`)

## 10. Deliverables & submission

- [ ] Saved Plant 3D project (30% of module marks)
- [ ] Data Manager → Project Reports → Engineering Items for the current drawing
- [ ] Export to Excel, saved inside the project folder
- [ ] In Excel, type name and student number at the bottom, font size `36`, save
- [ ] Print the final page only, landscape, one page wide
- [ ] Save the project, ZIP and upload
- [ ] Name and student number on the assignment
- [ ] Equipment, line and valve tags complete — no `?` placeholders
- [ ] Supports added

`<TBC>`: deadline (brief says only "END Week 9"), upload location, zip file name, paper size, whether the printout is uploaded (PDF?), late penalty (A1 was 5% per day). Isometrics and orthographic drawings are **not** required for A2.

## 11. Conflicts to confirm

- Pump datasheet table shows 6" suction / 4" discharge, ANSI 150#; text says `100` / `80`, `PN10`. Text presumably governs — confirm.
- Which `E-101` nozzles serve the `80` supply/return circuits and the `100` return to furnaces is not stated.
- Description for this A2 drawing reads `A1 Surname FirstName`.
- Ladder position: earlier notes said "south-west corner"; the brief says west wall toward the south end, not at the corner.
