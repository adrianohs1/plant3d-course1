# A2 step help (steps 2–12 of `late-fast-track.md`)

Practical help for each fast-track step, from the Week 5–9 Applied Notes and the Week 8 supports slides. Values are in `spec-summary.md`. Where the notes give no Plant 3D command, the text says so and marks the suggestion as mine.

Common to every step: set size, spec `10HC01` and line number before clicking Route Pipe. Fix placed parts with grips (up arrow = elevation, blue square = move, grey + = continue or branch, down arrow = Substitute Part), not by deleting.

## Step 2 — Pumps `P-301`, `P-302`
- Click the pump body; a pencil appears at each nozzle. Edit it: Type Straight Nozzle, units mm, FL, Pressure Class `10`, DIN 2632. Suction size `100`, discharge `80`. Under Select Nozzle click the new line, then Close.
- Do not use Add Nozzle to edit: it creates a new nozzle every click. Delete any extra. The tutorial default of 80 on the suction is wrong for the brief.
- Plinth `150` and 800 between baseplates (1181 centre to centre, base 381). Move with `3DMOVE` (axis arrow, type the distance, Enter). The notes do not give a plinth command; my suggestion is an AutoCAD `BOX` 150 high, with the pump at `EL 150`.
- Check: read every nozzle value back (the lecturer marked "100%?"); tags show no `?`; each nozzle node (circle with an X) is live.

## Step 3 — Furnaces and `E-101`
- Furnaces: Modify Equipment (right-click) D `1000`, W `1500`, H `1500`, Cube. One common `150` plinth about 4000 wide (my `BOX` suggestion), base `EL 150`, gap `1000` face to face. Two `80` nozzles each (mm, FL, class 10, DIN 2632): `EL 1200` = outlet to the header, `EL 700` = return inlet, facing the west header. Delete spare nozzles.
- `E-101`: shell and tube, `4000` overall, `450`, capped ends, centred on the north wall (X = 4500), centreline `1200`; two saddles near the quarter points on `150` plinths (my suggestion). Nozzles with the pencil: N1 `100` at 400 from the east end; N2 `80` at 675 from the east end; N3 `80` at 675 from the west end; N4 `100` at 400 from the west end; all pointing up.
- Check: tags `F-101`, `F-102`, `E-101` with no `?`; every nozzle mm, FL, class 10, DIN 2632; nodes live.

## Step 4 — Header and furnace lines
- Header `DN150`, `10HC01`, X = 300, 4000 long, centreline at pump suction level (`EL 520` in the working model; proposed Y span 5000–9000 if the model has none). Blank flange at each extreme end (part name not in the notes; pick from the 10HC01 flanges).
- Furnace lines `DN100`, `10HC01`: from each `EL 1200` outlet west to the header. If a drop misses X = 300, drag the end grip or use Move Part, then stub in with `ST`. Merge into a common line before the header; inline DN100 flanged flow meter there (nearest catalog part, labelled). Butterfly shut-off valve (hand lever) at each furnace exit; hover on the pipe until it snaps, then click.
- Check: line numbers show in Properties; no open nodes; header elevations right; Z-bends, not long straight runs.

## Step 5 — Pump branches, discharge, `E-101` outlet
- Suction branches `DN100`: reducing tee or stub-in 150×100 off the header (`ST`, or the grey + grip on the header). Falling to the pump with no pockets.
- Discharge `DN80`: non-return valve then isolating valve per pump; common DN80 line to `E-101` N4 via an 80×100 reducer. Rise all the way or add a vent at the high point.
- `E-101` N1 outlet `DN100`: east side to each furnace `EL 700` return inlet; double-regulating valve to each furnace and an isolating butterfly valve at each furnace return. Tag every valve `HA-1xx`.
- Check: line numbers; no open nodes; the loop is furnaces → header → pumps → `E-101` → furnaces; nothing across the middle of the floor at low level.

## Step 6 — DN80 supply, return and bypass
- **Resolved (2026-11-24, inferred):** `E-101` has four nozzles; the primary loop uses two (pump discharge in, outlet to the furnaces), so the two `80` nozzles N2 and N3 are the supply and return. The Week 9 sketch also has the 80 lines leaving the heat exchanger. Supply from N3 (west, nearest the exit); return into N2 (east). No DN80 line connects to the header; the header's blank flanges stay at both extreme ends.
- Lines `DN80`, `10HC01`, blue, separate line numbers: up to `EL 3700` (up-arrow grip, BOP/COP/TOP, type the value), west along the north wall as a grouped pair, out through the north wall west side, flange at the grid boundary (`Y = 12000`). Prefer Z-bends. Keep clear of the stair landing and ladder.
- Bypass: simple tee on each line (no 3-way valve), `DN80` bypass between them with a double-regulating valve, ball isolating valves and flanges at the tee outlets. Supply: isolating ball valves before and after the bypass position. Return: double-regulating valve before the bypass intersection.
- Check: line numbers; flanged ends at the boundary; `EL 3700`; valves tagged.

## Step 7 — Drains
- DN25 ball drain valve at the low point of each pump suction branch (branch down with a grey + grip or Route Pipe). Tie both into one `DN25` common line, valved, down to `EL 200` and ended with a flange. Tie in the bypass drain. Keep it against a wall or equipment base.
- Check: a drain before each pump; common drain at `EL 200`; no open nodes; all drain valves tagged.

## Step 8 — Valve tags and extra valves
- Every valve: unique `HA-1xx` tag from the P&ID number, size written beside it; no `?`. Operator via Properties (hand lever or handwheel).
- Expected valves: furnace-exit butterfly; furnace-return isolating butterfly; double-reg to each furnace; pump discharge non-return and isolating; supply ball isolating before and after the bypass; double-reg on the return and in the bypass; bypass tee-outlet ball valves; DN25 drains; flow meter.
- Worthwhile extras (the lecturer allows them): vent at a discharge high point; isolating valve on each suction branch at the header; pressure gauge on a 15 mm branch with an isolating valve and a 50×15 reducer on each discharge.

## Step 9 — Steel (simple version)
- Grid `0, 9000` × `0, 12000`, platforms `0, 5000, 10000` (UCS ticked, font 500); extra lines 1000 in from the ends for the stairs; `EXPLODE` only to remove a stray line.
- Members: DIN, IPE beams, HEA columns; columns first, then beams (Ctrl + right-click → Endpoint); Edit Structure to put top of steel on the grid line; Line Model while placing, Shape Model to check.
- Platform: Plate → Create Plate/Grate, Grate, ASTM, justification Bottom, New rectangular, corners on the beam tops; openings for stairs, ladder and pipe.
- Stairs east, north–south: width `800`, max tread `250`, stringer `U-200`. Ladder on the west wall near the south end, outside the footprint (cage on, radius `350`, start `2800`, max distance `1500`, stand-off `200`, Ortho on). Railings at default with gaps at the stairs and ladder; footings under every column; trim or mitre; close plate gaps; `GRID` layer off; save.
- Check: levels match the grid; handrails; no clash with the `EL 3700` run or the wall pipe pairs; access to pumps, valves and furnace fronts.

## Step 10 — Head heights, trip hazards, grouping, supports
- Head heights: anything over a walkway at BOP ≥ `2200`; fix with the up-arrow grip. Trip hazards: no floor-level run across the middle of the room or the stair and ladder approach. Grouping: a pair along the east wall (`E-101` to the furnaces) and a pair along the west wall (past the pumps), at matching elevations.
- Supports (Week 8 slides): group lines to minimise structures; route close to grade or steel; support near valves, flanges and heavy loads; keep load off nozzles; follow the project span table. The brief gives no span table; my rule of thumb is about every 3 m on DN80–DN150 and beside each valve and flange. The notes do not name the Plant 3D supports command; look for it on the Home tab or tool palette. Add at least a few supports to each grouped run.

## Step 11 — Report
- Save the drawing. Home → Data Manager → Project Reports → Engineering Items for `TC 3D Layout`. Export to Excel with Displayed data and Active node only; save inside the project folder.
- In Excel type name and student number at the bottom, font size `36`; save.
- Check: no blank tags or `?`; every pipe row has a line number; pump rows show their nozzle sizes; quantities plausible (if empty, wrong node or an unsaved drawing).

## Step 12 — Print, zip, upload
- Print only the final page: landscape, one page wide, A4 (assumed). Also save a PDF into the project folder (covers both readings).
- Save with the P3D icon → Save (not Save As); close the drawing and project; reopen once to confirm, then close.
- Zip the project folder as `A2 Surname Firstname.zip`; open the zip to confirm the drawing, project files and report are inside.
- Upload through Canvas; keep the confirmation (screenshot with the time). Then message the lecturer with the upload time and ask him to confirm receipt (late-submission message in `late-fast-track.md`).
