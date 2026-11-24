;;; a2_guides.lsp
;;; Guide lines for A2 steps 4-7 in TC 3D Layout.dwg. They are plain 3D
;;; polylines on their own layers, NOT Plant 3D pipes: route the real pipe
;;; in Plant 3D by snapping (Endpoint) to the guide corners, then delete
;;; the guides with A2GUIDEDEL before you submit.
;;; Load: APPLOAD, pick this file.
;;;
;;; A2GUIDES   - draws all guides (World coordinates, mm). Layers:
;;;              A2-GUIDE-S4 red     furnace lines, overhead at EL 2300
;;;              A2-GUIDE-S5 yellow  pump suction, pump discharge, HX outlet
;;;              A2-GUIDE-S6 blue    DN80 supply/return at EL 3700 + bypass
;;;              A2-GUIDE-S7 green   DN25 drains to EL 200
;;; A2GUIDEDEL - erases every polyline on the A2-GUIDE-* layers (only those).
;;;
;;; Measured from the drawing (2026-11-24): furnace F-102 outlet nozzle
;;; (4971, 2270, 1200); header centreline X 283, EL 520, Y 4914..8857;
;;; E-101 centre Y 11200, N1..N4 at X 5100 / 4825 / 2175 / 1900.
;;; ASSUMED (snap to the real nozzle, not the guide end, where they differ):
;;;  - F-101 outlet at (2971, 2270, 1200); both furnace returns directly
;;;    below their outlets at EL 700.
;;;  - pump suction at the WEST end (X 1590) at EL 520; discharge on top
;;;    near X 1900. If the suction is at the east end, rotate the pumps
;;;    first (next-steps section 2).
;;;  - E-101 nozzle tops at EL 1725; north boundary at Y 12000.
;;;  - HX outlet runs down X 6000: check it clears the stairs on the east side.
;;; Both commands use the World UCS while they run and put yours back.

(defun a2g-poly (lay pts)
  (setvar "CLAYER" lay)
  (command "_.3DPOLY")
  (foreach p pts (command p))
  (command ""))

(defun a2g-layer (name col)
  (command "_.-LAYER" "_M" name "_C" col "" ""))

(defun c:A2GUIDES (/ oldos oldlay oldecho)
  (setq oldecho (getvar "CMDECHO") oldlay (getvar "CLAYER") oldos (getvar "OSMODE"))
  (setvar "CMDECHO" 0)
  (setvar "OSMODE" 0)
  (command "_.UCS" "_W")
  (a2g-layer "A2-GUIDE-S4" "1")
  (a2g-layer "A2-GUIDE-S5" "2")
  (a2g-layer "A2-GUIDE-S6" "5")
  (a2g-layer "A2-GUIDE-S7" "3")

  ;; Step 4 - furnace outlets (EL 1200) north, up to EL 2300, west overhead,
  ;; down the west wall into the top of the header (EL 604 = 520 + 84).
  (a2g-poly "A2-GUIDE-S4" '((2971 2270 1200) (2971 2600 1200) (2971 2600 2300)))
  (a2g-poly "A2-GUIDE-S4" '((4971 2270 1200) (4971 2600 1200) (4971 2600 2300)
                            (2971 2600 2300)))
  (a2g-poly "A2-GUIDE-S4" '((2971 2600 2300) (283 2600 2300) (283 5200 2300)
                            (283 5200 604)))

  ;; Step 5a - pump suction branches off the header (DN100).
  (a2g-poly "A2-GUIDE-S5" '((283 7219 520) (1590 7219 520)))
  (a2g-poly "A2-GUIDE-S5" '((283 8400 520) (1590 8400 520)))
  ;; Step 5b - pump discharge (DN80): up to EL 2300, common line north
  ;; at X 1900, down into E-101 N4 (pointing up).
  (a2g-poly "A2-GUIDE-S5" '((1900 7219 812) (1900 7219 2300) (1900 8400 2300)))
  (a2g-poly "A2-GUIDE-S5" '((1900 8400 812) (1900 8400 2300) (1900 11200 2300)
                            (1900 11200 1725)))
  ;; Step 5c - HX outlet N1 (DN100): up to EL 2600 (above the furnace
  ;; lines), east to X 6000, south, west along Y 3000, drop to each furnace
  ;; return at EL 700.
  (a2g-poly "A2-GUIDE-S5" '((5100 11200 1725) (5100 11200 2600) (6000 11200 2600)
                            (6000 3000 2600) (4971 3000 2600) (2971 3000 2600)))
  (a2g-poly "A2-GUIDE-S5" '((4971 3000 2600) (4971 3000 700) (4971 2270 700)))
  (a2g-poly "A2-GUIDE-S5" '((2971 3000 2600) (2971 3000 700) (2971 2270 700)))

  ;; Step 6 - DN80 supply from N3, return into N2, up to EL 3700, grouped
  ;; along the north wall, out through the north wall west side at Y 12000.
  (a2g-poly "A2-GUIDE-S6" '((2175 11200 1725) (2175 11200 3700) (2175 11600 3700)
                            (600 11600 3700) (600 12000 3700)))
  (a2g-poly "A2-GUIDE-S6" '((4825 11200 1725) (4825 11200 3700) (4825 11850 3700)
                            (850 11850 3700) (850 12000 3700)))
  ;; bypass between the pair (simple tee each end)
  (a2g-poly "A2-GUIDE-S6" '((1200 11600 3700) (1200 11850 3700)))

  ;; Step 7 - DN25 drains: low point of each suction branch down to EL 200,
  ;; common line along X 1000 to the drain point.
  (a2g-poly "A2-GUIDE-S7" '((1000 7219 520) (1000 7219 200)))
  (a2g-poly "A2-GUIDE-S7" '((1000 8400 520) (1000 8400 200) (1000 7219 200)
                            (1000 6900 200)))

  (setvar "CLAYER" oldlay)
  (command "_.UCS" "_P")
  (setvar "OSMODE" oldos)
  (setvar "CMDECHO" oldecho)
  (princ "\nA2GUIDES: 15 guide polylines drawn on A2-GUIDE-S4..S7.")
  (princ "\nRoute each pipe in Plant 3D snapping to the corners; snap to real nozzles where they differ.")
  (princ "\nRun A2GUIDEDEL before you submit.")
  (princ))

(defun c:A2GUIDEDEL (/ ss)
  (setq ss (ssget "_X" '((0 . "POLYLINE") (8 . "A2-GUIDE-S4,A2-GUIDE-S5,A2-GUIDE-S6,A2-GUIDE-S7"))))
  (if ss
    (progn (command "_.ERASE" ss "")
           (princ (strcat "\nA2GUIDEDEL: erased " (itoa (sslength ss)) " guide polylines.")))
    (princ "\nA2GUIDEDEL: no guides found."))
  (princ))

(princ "\nA2 guides loaded: A2GUIDES, A2GUIDEDEL.")
(princ)
