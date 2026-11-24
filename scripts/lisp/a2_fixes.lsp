;;; a2_fixes.lsp
;;; A2 fixes for TC 3D Layout.dwg (from model-review-2026-11-24.md).
;;; Load: APPLOAD, pick this file. Then type the command names below.
;;; Coordinates are World (WCS), mm, read from the drawing on 2026-11-24.
;;;
;;; A2PLINTH  - draws the missing common 150 furnace plinth (3D solid box)
;;;             under F-101 and F-102: X 2371..5571, Y 594..2370, Z 0..150
;;;             (furnace bodies X 2471..5471, Y 694..2270, base EL 150,
;;;             plus 100 margin on each side). Layer A2-PLINTH.
;;; A2SELF102 - SELECTS (does not delete) the old F-102 line: 19 objects
;;;             (pipes, elbows, connectors, the 50 mm part at the furnace
;;;             exit, the stray 25 mm stub). Look at what is highlighted,
;;;             then press Delete yourself. Only Plant 3D pipe parts are
;;;             picked; it aborts if the header (58C, 604, 629) or any
;;;             equipment would be included.
;;; Both commands switch to the World UCS while they run and put yours back.

(defun a2-world-osnap-off (/ old)
  (setq old (getvar "OSMODE"))
  (setvar "OSMODE" 0)
  (command "_.UCS" "_W")
  old)

(defun a2-restore (oldos)
  (command "_.UCS" "_P")
  (setvar "OSMODE" oldos))

(defun c:A2PLINTH (/ oldos oldlay oldecho)
  (setq oldecho (getvar "CMDECHO"))
  (setvar "CMDECHO" 0)
  (setq oldlay (getvar "CLAYER"))
  (setq oldos (a2-world-osnap-off))
  (command "_.-LAYER" "_M" "A2-PLINTH" "_C" "8" "" "")
  ;; first corner, then the opposite corner with a different Z = height 150
  (command "_.BOX" '(2371.0 594.0 0.0) '(5571.0 2370.0 150.0))
  (setvar "CLAYER" oldlay)
  (a2-restore oldos)
  (setvar "CMDECHO" oldecho)
  (princ "\nA2PLINTH: furnace plinth drawn, 3200 x 1776 x 150, top at EL 150.")
  (princ "\nCheck: orbit once - 150 high, furnaces sit on it, clear of the header and pumps.")
  (princ))

(defun c:A2SELF102 (/ handles banned ok ss e typ n np nc ni bad)
  (setq handles '("6B7" "6D1" "6D6" "6DB" "6DE" "6E1" "6E6" "6E9" "6EE" "6F1"
                  "6F6" "6F9" "6FE" "73A" "73F" "788" "78D" "790" "795")
        banned  '("58C" "604" "629")   ; header pipe and its two end parts
        ok      '("ACPPPIPE" "ACPPCONNECTOR" "ACPPPIPEINLINEASSET")
        ss (ssadd) n 0 np 0 nc 0 ni 0 bad nil)
  (foreach h handles
    (if (and (setq e (handent h)) (entget e))
      (progn
        (setq typ (cdr (assoc 0 (entget e))))
        (cond
          ((member h banned) (setq bad T))
          ((not (member typ ok)) (setq bad T))
          (T (ssadd e ss) (setq n (1+ n))
             (cond ((= typ "ACPPPIPE") (setq np (1+ np)))
                   ((= typ "ACPPCONNECTOR") (setq nc (1+ nc)))
                   (T (setq ni (1+ ni)))))))))
  (cond
    (bad
      (princ "\nA2SELF102: stopped - a handle points at something that is not an F-102 pipe part.")
      (princ "\nNothing selected. Select the F-102 line by hand instead."))
    ((> n 0)
      (sssetfirst nil ss)
      (princ (strcat "\nA2SELF102: selected " (itoa n) " of 19: "
                     (itoa np) " pipes (expect 5), " (itoa nc) " connectors (expect 9), "
                     (itoa ni) " inline parts (expect 5)."))
      (princ "\nCheck the highlight runs from the F-102 exit to near the header only, then press Delete. Esc cancels."))
    (T (princ "\nA2SELF102: none found. Select the F-102 line by hand instead.")))
  (princ))

(princ "\nA2 fixes loaded: A2PLINTH, A2SELF102.")
(princ)
