# A2 model review — 2026-11-24

Review of `TC 3D Layout.dwg` (Drive, course folder; last saved 2026-11-24 22:04 UTC) against the 12 steps in `late-fast-track.md`. Read with `ezdwg` 0.22 (DWG reader) from the drawing's stored geometry. The DWG holds no tags, line numbers or nozzle size/class/standard: Plant 3D keeps those in the project database (`Piping.dcf`), so those items are marked "can't see".

Confidence: **[measured]** = read from the geometry; **[likely]** = part identified from its size and shape; **[can't see]** = not in the DWG.

## What the drawing contains

5 equipment, 6 pipes, 7 inline parts (elbows, flanges, possibly one valve), 9 connectors (all on the F-102 line), 1 structure grid, 2 solids (the pump plinths). No steel members, no supports.

## Step by step

| Step | Status | Evidence | Fix |
|---|---|---|---|
| 1 Setup | Can't see | Folder name, DWG number and description are not in the DWG. | Check in Project Manager. |
| 2 Pumps | Placed; nozzles not checked | [measured] Each pump on its own 1520×580×150 plinth; centres Y 7219 and 8400 (1181 c/c, 800 between baseplates). [can't see] Nozzle size and class. | Read back every pump nozzle (the lecturer's "100%?" item). Check the east end, about 100 past the plinth: if it is the suction, it faces away from the header. |
| 3 Furnaces, `E-101` | Placed; furnace plinth missing | [measured] Furnaces 1000 × 1500 × 1500, base `EL 150`, 1000 gap, south end; the only two solids are the pump plinths, so the furnaces have no plinth. [measured] `E-101` 4000 long, centreline `EL 1200`, centred at X = 3500 (planned 4500: harmless). [likely] Furnace nozzles on the north face. [likely] `E-101` sticks out 300 sideways as well as up, so at least one nozzle may point sideways. No saddles. | Add the common 150 furnace plinth. Check N1–N4 all point up. |
| 4 Header, furnace lines | Partly done, with errors | [measured] Header DN150, centreline `EL 520`, about 3960 long, X ≈ 283. [likely] End parts at both ends; south one 22 thick (blank), north one 55 (more like a weld-neck flange); no gaskets. F-102 line [measured]: DN80 not DN100, no reducers; runs west across the room at `EL 1200` (Y ≈ 3470, X 4857 → 1085); ends at X 971, about 690 short of the header (not connected); a 25 mm stray pipe overlaps it at the furnace exit. [likely] A 50 mm part at the F-102 exit (flange or butterfly valve). No F-101 line, no flow meter. | Delete the F-102 line and the stray stub. Redo it in DN100 with a 100×80 reducer at each nozzle, along the wall, stubbed into the header. Add the F-101 line, the common line, the flow meter and butterfly valves at both furnace exits. Make both header ends blind flanges. |
| 5 Pump branches, discharge, HX outlet | Not started | [measured] No pipe touches the pumps or `E-101`. | As written. |
| 6 DN80 supply, return, bypass | Not started | Nothing reaches `EL 3700`. | As written. |
| 7 Drains | Not started | No DN25 pipe. | As written. |
| 8 Valve tags | Can't see | At most one valve exists. | Tag valves while doing steps 4–7. |
| 9 Steel | Grid only | [measured] Grid present; no beams, columns, platforms, stairs, ladder, railings or footings. The grid reads Y 400–12400 and Z 505–10505, not 0–12000 and 0/5000/10000 (may be a decoding error). | In Plant 3D, `ID` a grid corner: if it is not (0,0,0), the platforms sit 505 high. Build the simple version last. |
| 10 Head heights, supports | Not started | No supports. The F-102 line at `EL 1200` across the room is a head-height and walkway problem. | The F-102 reroute fixes the crossing; add supports at the end. |
| 11 Report | Not started / can't see | Not in the DWG. | As written. |
| 12 Submit | Not started / can't see | Not in the DWG. | As written. |

## Fix order (cheapest marks first)

1. Furnace plinth.
2. Redo the F-102 line; add the F-101 line, the common line and the flow meter.
3. Step 5, then steps 7 and 8.
4. Steps 11–12.
5. Steel and supports last.

## Still open

- Zip name: `spec-summary.md` §14C says "name the zip like the project folder" (`A1 A2 Surname Firstname`), while the fast track says `A2 Surname Firstname.zip`. Not decided.
- Steps 1, 2, 8 and 11 need the zipped project folder or the Engineering Items export to verify.
