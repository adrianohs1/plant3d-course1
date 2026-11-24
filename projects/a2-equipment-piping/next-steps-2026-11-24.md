# A2 next steps — continue in the existing model

Decision 2026-11-24: keep working in `TC 3D Layout.dwg`; do not start over. Equipment, pump plinths, header and grid are usable; what is wrong is limited to the F-102 line and the missing furnace plinth (`model-review-2026-11-24.md`). Coordinates below are World (WCS), mm, read from the drawing saved 2026-11-24 22:04 UTC. "Proposal" marks my routing suggestion, not the lecturer's.

## 0. Three checks first (5 min)

| Check | How | If it fails |
|---|---|---|
| Drawing belongs to the project | Open it from Project Manager (Plant 3D Drawings) | Create a new 3D drawing in the project and copy the equipment, plinths and header into it |
| Grid origin | `ID`, click the grid's south-west corner | If not about `0,0,0` (reads `0,400,505`), move the grid by `0,-400,-505` |
| Line numbers | Click the header, Properties | If no line number or not `10HC01`, set them before routing anything else |

## 1. Load the helper (`scripts/lisp/a2_fixes.lsp`)

`APPLOAD`, pick the file, Load. Two commands:
- `A2SELF102` selects the old F-102 line (19 objects). Check the highlight, then press Delete.
- `A2PLINTH` draws the common furnace plinth: X 2371–5571, Y 594–2370, Z 0–150 (100 margin round both furnaces), layer `A2-PLINTH`.

Orbit once after `A2PLINTH`: the box should be 150 high with both furnaces sitting on it. Save, close and reopen the drawing after both.

## 2. Equipment read-back (pencil on each nozzle)

| Item | Where in the model | Set |
|---|---|---|
| `F-101` | X 2471–3471, Y 694–2270 | Nozzles `80`, mm, FL, class 10, DIN 2632; outlet `EL 1200`, return `EL 700`, both on the north face (likely X 2971, Y 2270) |
| `F-102` | X 4471–5471, Y 694–2270 | Same; outlet nozzle at X 4971, Y 2270, `EL 1200` (measured) |
| `E-101` | X 1500–5500, centre Y 11200, centreline `EL 1200` | N1–N4 all pointing **up** (one points sideways now). N1 X 5100, N2 X 4825, N3 X 2175, N4 X 1900 |
| `P-301`, `P-302` | X 1590–3159, centres Y 7219 and 8400 | Suction `100`, discharge `80`, mm, FL, class 10, DIN 2632. **Check which end is the suction:** it must face the header (west). If the suction is at the east end, rotate both pumps 180° before step 5 |

## 3. Furnace lines (proposal; changes the written plan)

`DN100`, `10HC01`, one line number per furnace line plus one for the common line. **This changes step 4 of `step-help.md` and `late-fast-track.md`**, which say "along the wall, not across the room". With the nozzles on the north face, any route to the west header must cross the south part of the room; the old line did it at `EL 1200` (head-height hazard). This route crosses overhead instead, at ≥ 2200 BOP (centreline `EL 2300`, BOP ≈ 2243). If you accept it, those two files get updated to match.

1. At each `EL 1200` outlet: 100×80 reducer, then the butterfly shut-off valve (hand lever).
2. North to Y 2600, then up to `EL 2300`.
3. `F-102` west along Y 2600 to X 2971; tee into the `F-101` riser there. From the tee this is the common line.
4. Common line west along Y 2600 to X 283, then north along the west wall to Y 5200, then down into the top of the header (stub-in `ST`, 150×100).
5. Flow meter (inline DN100 flanged) on the common line between X 2000 and X 1000.
6. Vent (small ball valve) at the high point, on top of the common line at `EL 2300`.

Check: no open nodes; the line at the west wall stays clear of the ladder (west wall near the south end); nothing below `EL 2200` crosses the floor.

## 4. Then continue the fast track

| Order | Step (`late-fast-track.md`) | Key points |
|---|---|---|
| 1 | 5 — pump suction and discharge | 150×100 stub-ins off the header (X 283, `EL 520`, Y 4914–8857) to each pump; discharge non-return + isolating valve, common DN80 into N4 (X 1900) via 80×100 reducer |
| 2 | 5 — HX outlet to furnaces | N1 (X 5100) `DN100` down the east side to each `EL 700` return, 100×80 reducer at each nozzle, double-reg + butterfly valve per furnace |
| 3 | 7 — drains | DN25 ball valve before each pump; common DN25 to `EL 200` |
| 4 | 6 — DN80 supply/return + bypass | From N3 (X 2175) and into N2 (X 4825), up to `EL 3700`, out the north wall west side |
| 5 | 8 — valve tags | `HA-1xx` on every valve |
| 6 | 11–12 — report and submit | Before steel, so marks are banked |
| 7 | 9–10 — steel and supports | Simple version last |

After each step: save, then put the drawing (or better, the zipped project) in the course Drive folder and I will re-check it.
