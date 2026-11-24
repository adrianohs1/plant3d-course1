# Assessment 2 — Step-by-step build guide

Companion to `build-checklist.md`. Values come from `spec-summary.md` (sections 1–14), the approved decisions and the Week 5–9 notes. Commands are as taught in those notes. Where the model already exists, **verify instead of rebuilding** and fix with grips or Modify Equipment, not by deleting. Coordinates marked *(proposed)* are not in the brief: keep your model's existing values if you have them.

A2 is late. Submit as soon as the checks in step 10 pass, and tell the lecturer.

## Conventions used throughout
- Units mm. Model: +X east, +Y north, +Z up. Room 9000 (X) × 12000 (Y).
- Nozzles: mm, Pressure Class 10, DIN 2632, end type FL.
- Spec `10HC01` for all water lines (use `10HS01` only for a part the HC spec lacks).
- Line tag `size-spec-service-number`; valve tag `HA-1xx` with the size beside it.
- Pipe elevations: clearance 2100 + 100 beam = BOP 2200 where crossing a walkway.

## Step 1 — Project and drawing
1. Copy the A1 project. Rename the folder `A1 A2 Surname Firstname`.
2. New 3D Piping drawing `TC 3D Layout`. Properties: DWG Number `3D 001`, Description `A1 Surname FirstName` (as the brief says).
3. Save with the P3D icon → Save (not Save As). Close and reopen to confirm.
4. Check: workspace is 3D Piping (Workspace Settings → 3D Piping if the ribbon is wrong).

## Step 2 — Grid and steel (Structure tab)
1. Create Grid: Axis `0, 9000`; Row `0, 12000`; Platform `0, 5000, 10000`. UCS ticked, font size 500.
2. Add grid lines 1000 in from the ends for the stair landing and stair width (edit the grid; to remove a line, EXPLODE and delete).
3. Display: Line Model while placing, Shape Model to check.
4. Member Settings: DIN, IPE (beams) and HEA (columns). Columns first, then beams (Member → grid points; Ctrl + right-click → Endpoint). Copy Selection to repeat.
5. Beams: right-click → Edit Structure, put top of steel on the grid line.
6. Platform floor: Plate → Create Plate/Grate; Grate, ASTM, justification Bottom, New rectangular; pick two opposite corners on the beam tops. Leave openings for the stairs, the ladder and pipe penetrations.
7. Stairs (east side, running north–south): Stair Settings width `800`, max tread `250`, stringer `U-200`. Start at ground, end on the landing beam, pick the side.
8. Ladder (west wall near the south end, outside the footprint, not at the corner; serves LVL 1 at `5000`): Ladder Settings, Draw cage ticked, start height `2800`, max distance `1500`, cage radius `350`, stand-off `200`. Ortho on; start at ground, end straight above at the platform.
9. Handrails: Railing at default; Line Model, pick each open edge. Leave gaps at the stairs and ladder.
10. Footings: Footing Settings, then Footing at the base of every column.
11. Trim or mitre beam ends; close gaps between plates and beams (grips or MOVE; plates sit on the beam tops).
12. Turn the `GRID` layer off. Save.
13. Check [Steel]: levels match the grid elevations; handrails present; stair landing and ladder clear of the `EL 3700` run on the north wall.

## Step 3 — Furnaces `F-101` and `F-102`
1. Equipment: Heat Exchanger → Plate Frame, Cube shape. Dimensions D `1000`, W `1500`, H `1500`. Tags `F-101`, `F-102`.
2. Plinth: one common `150` plinth under both. Block base at `EL 150`.
3. Layout: south end, side by side along X, gap `1000` measured face to face. `F-102` is the one nearest the west header (Week 7 routes its `EL 1200` line west to the header at X = 300).
4. Nozzles (pencil on each nozzle, not Add Nozzle): two per furnace, Straight, `80` mm, FL, Pressure Class `10`, DIN 2632. `EL 1200` = outlet to the header. `EL 700` = return inlet. Nozzle face toward the header.
5. Check [Equipment]: plinth present, tags set, nozzle elevations correct (3DMOVE or Modify Equipment if not).

## Step 4 — Heat exchanger `E-101`
1. Equipment: Heat Exchanger → Shell and Tube. Overall length `4000`, capped ends, diameter `DN450` (450). Tag `E-101`.
2. Position: centred on the north wall (X = 4500), centreline `1200` above the floor. Two saddles near the quarter points on `150` plinths.
3. Nozzles (edit existing with the pencil; type Straight, mm, FL, class 10): N1 `100` at 400 from the east end; N2 `80` at 675 from the east end; N3 `80` at 675 from the west end; N4 `100` at 400 from the west end. All four point up.
4. Roles: N1 = outlet to the furnaces; N4 = inlet from the pump discharge (via an 80×100 reducer); N2 and N3 = the blue DN80 supply/return exiting at `EL 3700`.

## Step 5 — Pumps `P-301` and `P-302`
1. Equipment: Pump → Centrifugal. Tags `P-301`, `P-302`. Save the first pump's settings as a template and reuse them for the second.
2. West side, north of centre, stacked north–south. `150` plinth. Baseplate width 381, centres `1181` apart, so the gap between baseplates is `800`.
3. Nozzles (pencil): suction `100`, discharge `80`, both mm, FL, class 10, DIN 2632. Do not leave the tutorial default of 80 on the suction.
4. Check [Equipment]: this is the item the lecturer marked "100%?". Re-open both pumps and read every nozzle value.

## Step 6 — Header and main lines
1. Set size, spec and line number before clicking Route Pipe (Home → Part Insertion).
2. Header: `DN150`, `10HC01`, 4000 long, at X = 300 (300 from the west wall), centreline at pump suction level (`EL 520` in the working model). Blank flange at both extreme ends.
3. Furnace lines: `DN100`, `10HC01`, from each furnace `EL 1200` outlet to the header. Butterfly shut-off valve (hand lever) at each furnace exit. Merge the two lines into a common line before the header and fit the inline DN100 flanged flow meter there.
4. Pump suction: reducing tee or stub-in 150×100 off the header to each pump suction (ST command). Branch falls from the header to the pump with no pockets.
5. Pump discharge: DN80 `10HC01`, isolating valve plus non-return valve per pump, common line into `E-101` N4 via an 80×100 reducer.
6. HX outlet to furnaces: `100`, PN10, from N1 down the east side to each furnace. Double-regulating valve to each furnace; isolating butterfly valve at each furnace return inlet (`EL 700`).
7. Route as the lecturer's sketch: pairs along the east and west walls, loops down to the pumps, into each furnace from the side. Nothing across the middle of the floor.
8. Route method: Route Pipe, click the first nozzle node (circle with X), drag, click the second node; N or P cycles auto routes. Use Z-bends rather than long straight runs between fixed equipment.
9. Fix mistakes with grips (up arrow = elevation, square blue = move, + = continue, down arrow = Substitute Part), not by deleting.

## Step 7 — DN80 supply, return and bypass
1. `80` supply: from the north end of the header (via `E-101` N2/N3 circuit as modelled); `80` return to the south end. Grouped on the west wall, exiting the north wall, west side, at `EL 3700`, flange at the grid boundary. Blue.
2. Blank flanges at the extreme header ends; the DN80 tee-offs sit on short stubs inside them.
3. Bypass: `DN80` `10HC01` between supply and return. No 3-way valve: a simple tee at each end, ball isolating valves at the tee outlets, flanges, and a double-regulating valve in the bypass itself.
4. Isolating ball valves before and after the bypass position on the supply. Double-regulating valve on the return before the bypass intersection.

## Step 8 — Drains
1. Drain valve (DN25 ball) at the low point of each pump suction branch.
2. Common `DN25` line tying the pump drains and the bypass drain into one line, valved, down to grade at `EL 200`, ending in a flange.
3. Check [Piping]: every pump has a drain; the common drain reaches `EL 200`.

## Step 9 — Valves, tags, supports
1. Place valves from the palette: hover on the pipe until it snaps, click. Operator via Properties (hand lever or handwheel).
2. Tag every valve `HA-1xx` when prompted; write the size beside it. No `?` anywhere.
3. Line numbers: right-click each pipe → Properties and confirm the line tag (fix any lost by Line to Pipe).
4. Supports: add them to the grouped runs (at least several; Week 8 SUPPORTS method).
5. Check [Piping]: head heights (BOP ≥ 2200 across walkways), trip hazards (no floor-level runs across walkways), grouping, extra valves if you think they are needed.

## Step 10 — Report, print, zip, upload
1. Data Manager → Project Reports → Engineering Items for the current drawing. Export to Excel and save inside the project folder.
2. In Excel type your name and student number at the bottom, font size `36`. Save.
3. Print the final page only: landscape, one page wide, A4.
4. Save the project, zip the folder as `A2 Surname Firstname.zip`, upload through Canvas.
5. Final check against the lecturer's list: name and student number; layout matches the brief; steel levels and handrails; pump 100%; plinths; tags; valves; drains; head heights; trip hazards; grouping; supports; line numbers.
6. Message the lecturer about the late submission.

## What to do when a connection fails
- Nozzles will not connect: re-check mm, Pressure Class 10, DIN 2632, FL on both ends.
- Line number missing: set it in Properties.
- Routes will not snap: Isolate Objects to hide clutter, then End Object Isolation.
- Layout tabs missing: right-click the drawing area → Options → Display → Display Layout and Model tabs.
