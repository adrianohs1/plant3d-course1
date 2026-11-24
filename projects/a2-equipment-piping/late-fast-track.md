# A2 late-submission fast track

One page. Only the steps that carry marks on the lecturer's check list, in the order that gets a complete submission out soonest. Full detail is in `build-guide.md`; values are in `spec-summary.md`.

A2 is late. Message the lecturer first (draft below), then build.

## 0. Message the lecturer (send before building)

> Subject: MECH7022 Assessment 2 — late submission, [Surname Firstname], [student number]
>
> Hello [Lecturer's name],
>
> I have not yet submitted Assessment 2 (equipment and piping layout), which was due at the end of Week 9. I expect to upload it by [date/time] through Canvas. Could you confirm that I can still submit, and what penalty applies? I understand A1 lost 5% per day.
>
> Thank you,
> [Name], [student number]

Give a date you can keep.

## Build order (cheapest marks first)

| # | Do | Marks item | Check before moving on |
|---|----|-----------|------------------------|
| 1 | Open the saved model. Name the folder `A1 A2 Surname Firstname`; drawing `TC 3D Layout`, `3D 001`. | General | Opens after save, close and reopen. |
| 2 | Pumps `P-301`, `P-302`: edit each nozzle (pencil). Suction `100`, discharge `80`; mm, FL, class 10, DIN 2632. `150` plinth, 800 between baseplates. | Pump "100%?", plinths | Read every nozzle value back. |
| 3 | Furnaces `F-101`, `F-102`: `150` common plinth, two `80` nozzles each at `EL 700` (return) and `EL 1200` (outlet). `E-101`: `450`, 4000 long, centreline `1200`, N1–N4 `100/80/80/100`. | Equipment, plinths, tags | No `?` in any tag. |
| 4 | Header `DN150` `10HC01`, X = 300, 4000 long, blanks at both extreme ends. Furnace lines `DN100` (100×80 reducer at each `EL 1200` nozzle) north to Y 2600, up to `EL 2300` (BOP ≥ 2200), west overhead and down the west wall into the top of the header; never across the room at `EL 1200` (route: `next-steps-2026-11-24.md` §3); butterfly valves at the furnace exits, flow meter on the common line. | Piping, valves | Every pipe shows a line number in Properties. |
| 5 | Pump suction branches off the header (150×100 stub-in), DN80 discharge with non-return and isolating valves into `E-101` N4 via 80×100 reducer. HX outlet DN100 to each furnace with a double-reg valve and a 100×80 reducer at each `EL 700` nozzle. | Piping, valves | Every nozzle connects (no open nodes). |
| 6 | DN80 supply and return to the north wall, west side, `EL 3700`, flanged at the grid boundary. Bypass with simple tees, ball valves, double-reg valve. | Piping | Lines end in flanges at the boundary. |
| 7 | Drains: DN25 ball valve before each pump, common DN25 to grade at `EL 200`. | Drains | Both pumps drained; drain ends at `EL 200`. |
| 8 | Valve tags `HA-1xx` (size beside each valve). Add more valves where sensible. | Valves, tags | No `?`. |
| 9 | Steel, simple version: grid `0,9000` × `0,12000`, platforms `5000` and `10000`; grating with openings; stairs east (800 wide, 250 tread, U-200); ladder west wall near the south end (cage, start 2800, stand-off 200); railings with gaps; footings under columns; `GRID` layer off. | Steel, levels, handrails | Levels match the grid. |
| 10 | Head heights and trip hazards: anything over a walkway at BOP ≥ `2200`; no floor-level runs across walkways. Group runs along the walls. Add several supports. | Head heights, trips, grouping, supports | Walk the model in plan and 3D. |
| 11 | Data Manager → Project Reports → Engineering Items; export to Excel in the project folder. Name and student number at the bottom, font `36`. | Report | Excel saved inside the project folder. |
| 12 | Print the final page: landscape, one page wide, A4. Save, zip as `A2 Surname Firstname.zip`, upload through Canvas. | Submission | Upload confirmation on screen. |

## If time runs short
- A complete but plain model scores better than a polished one missing the report or the upload.
- Do steps 2, 3, 4, 5, 7, 8 and 11–12 before refining steel (step 9).
- Do not redo placed parts: fix with grips (up arrow = elevation, blue square = move, down arrow = Substitute Part).

## After uploading
- Tell the lecturer it is in, with the upload time.
