# Assessment 2 — Build-order checklist

Order of work in Plant 3D, tied to the lecturer's check list (Week 9). Values come from `spec-summary.md`; anything marked `<TBC>` there is still open. Tick each box in the model, not here, if you prefer. Check-list tags in brackets: [General] [Steel] [Equipment] [Piping].

## 0. Before you start
- [ ] Contact the lecturer about late submission if A2 is not yet in (planner marked it for the weekend of 22 November).
- [ ] Ask the open questions in `lecturer-questions.md` that block the build: header supply/return end, pump discharge pipework to `E-101`, flange standard for pumps and `E-101`.

## 1. Project and drawing [General]
- [ ] Copy the A1 project and rename the folder `A1 A2 Surname Firstname`.
- [ ] New drawing `TC 3D Layout`, DWG Number `3D 001`, Description `A1 Surname FirstName` (confirm A1 vs A2).
- [ ] Units mm. Save with the P3D icon → Save (not Save As). Close and reopen to confirm.

## 2. Grid and steel [Steel]
- [ ] Origin `0,0,0`. X `0, 9000`, Y `0, 12000`, Z `0, 5000, 10000`. Confirm orientation (Week 9 sketch has north to the left).
- [ ] Platforms at `5000` and `10000` (inferred, confirm). Levels match the grid elevations.
- [ ] Stairs on the east side, running north–south. Ladder on the west wall toward the south end, outside the footprint, not at the corner.
- [ ] Handrails, with gaps at stair and ladder access. Grating openings where pipes pass through platforms. Footings under columns at grade.
- [ ] Close gaps between plates and beams (grips or `MOVE`); plates sit on the beam tops.
- [ ] Turn off the `GRID` layer before plotting.

## 3. Equipment [Equipment]
- [ ] `F-101` and `F-102`: block D 1000, W 1500, H 1500 (as the brief states); 1000 gap; one common `150` plinth; south end, side by side.
- [ ] `E-101`: shell and tube, 4000 overall, capped ends, `DN450`, centreline `1200` above floor, against the north wall.
- [ ] `P-301` and `P-302`: centrifugal, `150` plinth, `800` gap, west side north of centre, stacked north–south.
- [ ] Plinths under the pumps and furnaces (lecturer checks this).
- [ ] Equipment tags set; none show `?`.

## 4. Nozzles [Equipment]
- [ ] Furnaces: two `80` nozzles each at `EL 700` and `EL 1200`; `PN10`, `FL`, `DIN 2632`.
- [ ] `E-101`: N1 `100` at 400 from the east end; N2 `80` at 675 from the east end; N3 `80` at 675 from the west end; N4 `100` at 400 from the west end.
- [ ] Pumps: suction `100`, discharge `80`, both `PN10`, `DIN`, mm. Recheck `P-301` and `P-302`; the lecturer marked the pump "100%?".

## 5. Header and pipework [Piping]
- [ ] Main header (LPHW return): `DN150`, `10HC01`, 4000 long, 300 from the side wall, at pump suction level, blank flange at both ends.
- [ ] Furnaces → header: `DN100`, `10HC01`. Header → pumps: suction `100`, each pump fed from the header.
- [ ] HX outlet → furnaces: `100`, `PN10`.
- [ ] `80` supply and `80` return (blue): exit the north wall, west side, at `EL 3700`, flange at the grid boundary.
- [ ] Bypass between supply and return: simple tee at each end (or the `10HS01` 3-way valve), valves and flanges at the tee outlets.
- [ ] Route as the lecturer's sketch: pairs along the east and west walls, loops down to the pumps, into each furnace from the side, nothing across the middle of the floor.

## 6. Valves and instruments [Piping]
- [ ] Butterfly shut-off valve (hand lever) at each furnace exit; isolating butterfly valve at each furnace return.
- [ ] Flow meter on the common line.
- [ ] Double-regulating valves: bypass, `80` return before the bypass intersection, and HX outlet to each furnace.
- [ ] Isolating ball valves before and after the 3-way position on the `80` supply.
- [ ] Every valve tagged from its P&ID number, `HA-1xx`; no `?`. Add more valves if needed (the lecturer allows it).

## 7. Drains [Piping]
- [ ] Drain valve before each pump.
- [ ] One common `DN25` drain valve and line from the `80` bypass to grade at `EL 200`.

## 8. Head heights, trip hazards, supports [Piping]
- [ ] Anything crossing a walkway at `2200` BOP or higher. Floor-level runs stay against walls or equipment.
- [ ] Piping grouped together.
- [ ] Add supports (at least a few on grouped runs; Week 8 method).

## 9. Deliverables [General]
- [ ] Name and student number on the assignment.
- [ ] Data Manager → Project Reports → Engineering Items for the current drawing.
- [ ] Export to Excel, saved inside the project folder. Type name and student number at the bottom, font size `36`, save.
- [ ] Print the final page only, landscape, one page wide.
- [ ] Save the project, zip it and upload. Confirm deadline, upload location, zip name and paper size with the lecturer.
- [ ] Isometrics and orthos are not required for A2.
