# Assessment 2 — Equipment Piping: Spec Summary

**Status:** DRAFT — merged from the A2 brief requirements checklist (source: `Assessment_2_Mid_Week_9.docx` plus the lecturer's Assessment 2 CHECK LIST). Anything the brief doesn't state is `<TBC>`.

## 1. Project & drawing setup

- Copy of A1 project; folder renamed `A1 A2 Surname Firstname`
- New drawing `TC 3D Layout`; DWG Number `3D 001`; Description `A1 Surname FirstName` (brief says A1 as written — confirm)
- Save with the P3D icon → Save (not Save As); close and reopen to confirm

## 2. Grid

- Origin `0,0,0`; X `0, 9000` (east/west); Y `0, 12000` (north/south); Z `0, 5000, 10000`
- `<TBC>` which end of X is east; that +Y is north (plan view: N up, stairs on the right/east)
- Week 9: the lecturer's routing sketch is drawn over the A2 plan view with **north to the left** (heat exchanger on the north wall, furnaces at the south end). This conflicts with the "N up" note above, so confirm the plan-view orientation.

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
| `E-101` | N1 | 100 | 400 from East end | `PN10`, `FL`, `DIN 2632` |
| `E-101` | N2 | 80 | 675 from East end | `PN10`, `FL`, `DIN 2632` |
| `E-101` | N3 | 80 | 675 from West end | `PN10`, `FL`, `DIN 2632` |
| `E-101` | N4 | 100 | 400 from West end | `PN10`, `FL`, `DIN 2632` |
| `P-301`, `P-302` | Suction | 100 | pump | `PN10` flange |
| `P-301`, `P-302` | Discharge | 80 | pump | `PN10` flange |
| Header | Both ends | `DN150` | blind flange | `10HC01` (PN10) |

Resolved 2026-11-24 (§14): furnace `EL 1200` = outlet, `EL 700` = return; `E-101` N1–N4 point up; N1/N4 = furnace loop, N2/N3 = DN80 return/supply; every nozzle mm, class 10, DIN 2632, FL.

## 5. Pipework & valves

| Line | Size / spec | Required |
|------|-------------|----------|
| Furnaces → header | `DN100`, `10HC01` | Butterfly shut-off valve (hand lever) at each furnace exit; flow meter on common line |
| Header → pumps | suction `100` | Each pump fed from header; drain valve before each pump |
| `80` supply | `80` | One end of header; isolating ball valves before and after the 3-way position; exits north wall, west side, `EL 3700`, flange at grid boundary |
| `80` return | `80` | Opposite header end; double-reg valve before bypass intersection; exits north wall, west side, `EL 3700`, flange at grid boundary |
| Bypass (supply → return) | `<TBC>` | Double-reg valve; 3-way valve omitted — simple tee at each end, valves and flanges at tee outlets |
| HX outlet → furnaces | `100`, `PN10` | Double-reg valve to each furnace; isolating butterfly valve at each furnace return |

Week 9: the `10HS01` palette has a 3-way temperature valve (`FL`, class 10); the brief allows a simple tee instead, so either is acceptable. Swap the operator (hand lever or handwheel) from the valve's Properties. Valve tags come from the P&ID number (e.g. `HA-1xx`).

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
- **Week 9 routing target (lecturer's sketch):** main lines (red and yellow) run as pairs around the edge of the room, not diagonally: one pair along the east side between `E-101` and the furnaces, another along the west side past the pumps. Pipes loop down to the pumps and enter each furnace from the side. The `80` lines (blue) leave `E-101` through the north-west corner (item 3.7: north wall, west side, `EL 3700`). No pipe crosses the middle of the floor at low level; floor-level runs stay against walls or equipment; anything crossing a walkway is at `2200` BOP or higher. Add at least a few supports in grouped runs (Week 8 method).
- **Course guidance (not in brief):** Week 7 tutorial — `2100` minimum clearance, `2200` BOP over a beam (this repo's README uses `>= 2200 mm` BOP over walkways)

## 9. Tagging

- Stated: `F-101`, `F-102`, `P-301`, `P-302`
- Check list requires line numbers and equipment tags
- Week 9: the lecturer's notes list `F-101`, `F-102`, `P-301`, `P-302` and `E-101` as the equipment tags, and valve tags take the P&ID number (e.g. `HA-1xx`)
- `<TBC>`: line number format (lecturer's sample uses `Size-Spec-Service-Number`)

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

Deadline: the brief says "END Week 9"; the Week 9 notes say the academic planner marks A2 at the weekend of 22 November, so if it isn't submitted, contact the lecturer about late submission now. `<TBC>`: upload location, zip file name, paper size, whether the printout is uploaded (PDF?), late penalty (A1 was 5% per day). Isometrics and orthographic drawings are **not** required for A2.

## 11. Conflicts to confirm

- Pump datasheet table shows 6" suction / 4" discharge, ANSI 150#; text says `100` / `80`, `PN10`. Text presumably governs — confirm.
- Which `E-101` nozzles serve the `80` supply/return circuits and the `100` return to furnaces is not stated.
- Description for this A2 drawing reads `A1 Surname FirstName`.
- Ladder position: earlier notes said "south-west corner"; the brief says west wall toward the south end, not at the corner.

## 12. Lecturer's check list (Week 9 notes)

| Area | He checks |
|------|-----------|
| General | Full name and student number on the assignment; overall layout matches the brief |
| Steel | Handrails; levels match the grid elevations |
| Equipment | Pump modelled correctly (he highlighted "100%?": suction `100` PN10, discharge `80` PN10, DIN, mm; recheck `P-301` and `P-302`); all equipment modelled; plinths under pumps and furnaces; equipment tags |
| Piping | Valves (add more if needed); drains allowed for; head heights; trip hazards; piping grouped together; supports |

## 13. Consistency check (2026-11-24)

Likely model problems:
1. **Header ends:** the brief wording ties the `80` supply and return to the header ends, but the nozzle count and the Week 9 sketch put them on `E-101` N2/N3. Resolved 2026-11-24: N3 supply, N2 return, no DN80 line on the header, blanks at both extreme ends. Residual risk: if the brief literally tees the DN80 lines off the header, a marker could read it differently; the check list does not test this.
2. **Pump sizes:** datasheet 6" / 4" is DN150 / DN100, not DN100 / DN80 (size difference, not only ANSI vs PN10). Text and Week 9 notes say DN100 / DN80 at PN10; the lecturer flagged the pump "100%?". Note the DN150 suction matches the header size.
3. **Stairs vs east run:** stairs on the east side (north–south) share the east wall with the lecturer's main pipe pair. Check clearances.
4. **Ladder vs west run:** ladder on the west wall toward the south end shares the wall with the west pipe pair past the pumps. Check clearances.
5. **Reducers:** DN100 lines meet DN80 furnace nozzles and a DN150 header; the brief gives no reducers, so add them.

Wording and dates:
6. Plan orientation: north up (spec) vs north to the left (Week 9 sketch).
7. Three deadline sources: "Mid Week 9" (brief file name), "END Week 9" (brief), weekend of 22 November (planner).
8. `A1` appears in the folder name `A1 A2 Surname Firstname` and the drawing description `A1 Surname FirstName`; likely a copy-paste leftover.
9. "Before and after the 3-way position" is ambiguous if a simple tee is used instead of a 3-way valve.
10. The header is called the LPHW return yet sits between furnaces and pumps; pump discharge to `E-101` is not given.

Checked and consistent: `E-101` (4 m) fits the 9 m north wall; furnaces plus the 1000 gap total 4 m; the ladder position agrees across the spec, checklist and brief.

## 14. Answers from the Week 5–9 notes and design assumptions (2026-11-24)

**Status:** the assumptions in part B and the additions in part C were reviewed and approved by the student on 2026-11-24. They are design decisions now, not open questions. A2 is late (the deadline has passed); late-submission terms are for the lecturer.

Source: the Applied Notes in the course Drive folder (secondhand summaries; the A2 brief itself is not in Drive).

### A. From the notes
- **Nozzles:** all nozzles mm, Pressure Class 10, DIN 2632, `FL` (furnaces, `E-101` N1–N4, pumps). Pumps: suction `100`, discharge `80` (brief page 4); the datasheet's 6"/4" does not govern. `P-301`/`P-302`: 1181 centre to centre, 381 base, so the 800 gap is between baseplates.
- **Header:** at X = 300 (west side); centreline `EL 520` in the working model.
- **Steel:** platforms 5000 and 10000; stairs width 800, tread 250, stringer U-200; ladder cage on, start height 2800, max distance 1500, cage radius 350, stand-off 200; extra grid lines 1000 in from the ends for the stairs; plate/grate ASTM, justification Bottom; DIN members. Keep the stair landing and ladder clear of the `EL 3700` run on the north wall.
- **Headroom:** 2100 clearance + 100 beam = `2200` BOP; `EL 1200` runs must not cross a walkway; use Z-bends for thermal expansion; pump suction falls from the header with no pockets.
- **Bypass:** per the Week 6 notes the brief omits the 3-way valve: simple tee at both ends, valves and flanges at the tee outlets.
- **Tags:** line tags `size-spec-service-number` (e.g. `150-10HS01-BFWS-1001`), valve tags `HA-1xx` with the size beside each valve; use the same line tag format in 3D.
- **Ladder conflict (unresolved):** Week 5 notes put the ladder at the south-west corner (brief page 5 suggested plan); the brief text is read as west wall toward the south end, not at the corner.

### B. Assumptions (inferred, not confirmed by the lecturer)
| Item | Assumption | Reason |
|------|------------|--------|
| Furnace nozzles | `EL 1200` = outlet to header; `EL 700` = return inlet | Week 7 runs the `F-102` `EL 1200` line west to the header; hot outlets sit high |
| Line spec | `10HC01` on all water lines; `10HS01` only for a part the HC spec lacks | Week 7: set spec before routing |
| Printout / upload | A4 landscape, final page only; zip named like the folder; late penalty 5%/day as A1 | Check list; A1 rule |
| Furnaces | On the 150 plinth, base `EL 150`, nozzle face toward the west header, gap measured face to face | Keeps the 1000 gap meaningful; header is west |
| `E-101` | Centred on the north wall (X = 4500), two saddles near the quarter points on 150 plinths | 4 m shell on a 9 m wall |
| `E-101` nozzles | DN100 pair N1/N4 = furnace loop; DN80 pair N2/N3 = blue supply/return exiting at `EL 3700`; pump discharge DN80 enters N4 via an 80×100 reducer; N1 feeds the furnaces | Sizes pair naturally; matches the lecturer's sketch |
| Pump discharge to `E-101` | DN80 `10HC01`; non-return plus isolating valve per pump; common line into N4 | Standard pump practice; extra valves allowed |
| Pump drains | DN25 ball valve at the low point of each suction branch, tied into the common DN25 line to grade at `EL 200` | Brief names the DN25 drain; low-point rule |
| Header ends / DN80 start | **Resolved:** supply from `E-101` N3 (west), return into N2 (east); no DN80 line connects to the header; blank flanges at both extreme header ends | `E-101` has four nozzles: the primary loop uses N1 and N4, so the two `80` nozzles N2/N3 are the supply/return; the Week 9 sketch has the 80 lines leaving the heat exchanger |
| Flow meter | Inline DN100 flanged meter on the common line where the furnace lines merge, before the header | Only place one meter covers both furnaces |
| Bypass | DN80 `10HC01`; ball isolating valves at the tee outlets; double-regulating valve in the bypass | Matches the lines it bridges |
| Pump branches | Reducing tee or stub-in 150×100 off the header, falling to the pump | Weeks 6–7 rules |
| Ladder and steel | Ladder serves LVL 1 (`5000`) with a cage; grating over the footprint with stair/ladder openings; DIN IPE/HEA; footings under every column | Tutorial settings |
| Orientation | Model +X east, +Y north; the sketch's "north left" is page rotation only | Relative layout is what matters |
| Description | Follow the brief literally (`A1 Surname FirstName`) | Template leftover; nothing hinges on it |

Still to confirm with the lecturer: pump discharge pipework, deadline and late terms, upload location.

### C. Further decisions (approved 2026-11-24)
- **Ladder:** on the west wall near the south end, outside the footprint, not at the exact corner. This satisfies both the brief text and the Week 5 suggested plan.
- **`E-101` nozzle directions:** all four (N1–N4) point up.
- **Pump datasheet:** the brief text governs (suction `100`, discharge `80`, `PN10`); the datasheet's 6"/4" is ignored.
- **Upload and zip:** upload through Canvas, as for A1; name the zip like the project folder (`A2 Surname Firstname.zip`).
- **Deadline:** passed; A2 is being submitted late.

## 15. Model as built (review 2026-11-24)

From `model-review-2026-11-24.md`. These differ from the plan above but are acceptable:
- Furnace nozzles are on the north face, not facing the west header. Route the furnace lines north out of the furnaces, up to `EL 2300` (BOP ≥ 2200), west overhead and down the west wall into the header (accepted 2026-11-24; `next-steps-2026-11-24.md` §3).
- `E-101` is centred at X = 3500, not 4500. Keep it; the brief only says "against the north wall".
- Reducers are needed wherever a DN100 line meets a DN80 furnace nozzle (100×80 at all four furnace nozzles), plus 150×100 at the pump branches and 80×100 into `E-101` N4.
