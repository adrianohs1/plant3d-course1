# Assessment 2 — Questions for the lecturer

Source: the `<TBC>` items in `spec-summary.md`.

## Submission
1. What is the exact deadline? The brief says only "END Week 9". *(Partly answered: the Week 9 planner marks A2 at the weekend of 22 November. Ask about late submission.)*
2. Where do I upload, what should the zip file be called, and is a late penalty applied? A1 was 5% per day.
3. What paper size is the final printout, and do I upload it as a PDF as well?

## Setup and conflicts
4. The drawing description reads `A1 Surname FirstName`. Is that intended for A2, or should it say A2?
5. The pump datasheet says 6" suction and 4" discharge at ANSI 150#, but the text says DN100 and DN80 at PN10. Does the text govern?
6. Which end of the X axis is east? Is +Y north? The plan view shows north up and the stairs on the right. *(Week 9 sketch shows north to the left, so please confirm the orientation.)*

## Equipment
7. For `F-101` and `F-102`, what are the insertion point, rotation, base height and nozzle face? Is the 1000 gap measured between faces or between centres?
8. Which furnace nozzle is the outlet and which is the return?
9. For `E-101`, where along the north wall does it sit, and how is the shell supported?
10. Which `E-101` nozzles (N1–N4) serve the DN80 supply and return circuits, and which serve the DN100 return to the furnaces? What are the nozzle directions?
11. For `P-301` and `P-302`, what are the coordinates, rotation and datasheet dimensions? Does the 800 gap apply to the baseplates or the plinths?

## Ratings and specs
12. What flange standard and rating apply to the `E-101` nozzles, the pump flanges and the header blind flanges?
13. What spec applies to every line except the header and the furnace-to-pump pipework?

## Pipework and valves
14. Which end of the header is supply and which is return?
15. Which side wall is the header 300 from? What are its Y start and end, and what is the "pump suction level" value?
16. Where exactly is the "common line" for the flow meter, and what type and size of meter is wanted?
17. What size and spec is the bypass? What valve type goes at the tee outlets?
18. What is the branch spec for the lines to the pumps?
19. The brief gives no pump discharge pipework to `E-101`. What size, spec, check and isolation valves, and nozzle does it need?
20. What are the size, type and drain destination of the drain valve before each pump?

## Steel and routing
21. What are the platform extent, member sizes, grating and plate, and stair width, tread and rise? Are the platforms at 5000 and 10000 (inferred from the LVL 0 and LVL 1 & 2 labels)?
22. Which level does the ladder serve, and does it have a cage? Where are the footings?
23. Does the Week 7 tutorial guidance apply, meaning 2100 minimum clearance and 2200 bottom of pipe over a beam? The brief itself gives no headroom, slope or support-spacing values. *(Partly answered: Week 9 notes say anything crossing a walkway is at 2200 BOP or higher. Slope and support spacing are still open.)*

## Tagging
24. What is the `E-101` tag, and which line-number format applies? The lecturer's sample uses `Size-Spec-Service-Number`. *(`E-101` answered in Week 9 notes; line-number format still open.)*
25. Do valve tags follow `HA-1xx`? *(Answered in Week 9 notes: valve tags take the P&ID number, e.g. `HA-1xx`.)*

## Ladder position
26. Earlier notes said "south-west corner", but the brief says the west wall toward the south end, not at the corner. Can you confirm the brief governs?
27. The header has blank flanges at both ends, but the `80` supply and return connect at opposite header ends. Where do the DN80 lines tee off relative to the blanks?
28. The pump datasheet's 6" suction and 4" discharge are DN150 and DN100, not DN100 and DN80. Is the datasheet or the text correct for the pump nozzles?
29. Should I add reducers where the DN100 lines meet the DN80 furnace nozzles and the DN150 header? The brief doesn't mention them.
30. If I use a simple tee instead of the 3-way valve, where exactly is the "3-way position" for the isolating ball valves?

## Answers and assumptions (2026-11-24)

The inferred answers (I) were reviewed and approved by the student on 2026-11-24 and are now design decisions. A2 is late; the deadline has passed.

Details are in `spec-summary.md` section 14. A = answered by the Week 5–9 notes; I = inferred, not confirmed.

- A: 5 (text governs: suction 100, discharge 80, PN10), 10 (N3/N4 match the brief), 11 (800 between baseplates), 12 (PN10, DIN 2632, FL on all nozzles), 15 (header at X = 300, west side, `EL 520` in the model), 21 (steel settings), 23 (2200 BOP; Z-bends), 24 and 25 (tag formats), 30 (simple tee at both bypass ends).
- I: 2 and 3 (A4 landscape, 5%/day), 4 (follow the brief literally), 6 (+X east, +Y north), 7, 8 (`EL 1200` = outlet), 9, 13 (`10HC01`), 14 and 27 (supply north end, return south end, blanks outside the tee-offs), 16, 17, 18, 19, 20, 22, 29 (add reducers).
- Decided 2026-11-24: 1 (deadline passed; submitting late), 2 (upload through Canvas; zip named `A2 Surname Firstname.zip`), 26 (ladder on the west wall near the south end, outside the footprint, not at the corner), 28 (text governs, same as 5), 10 (E-101 nozzles N1–N4 all point up).
- Still open: none that block the build. Only the lecturer can give the late-submission terms.
