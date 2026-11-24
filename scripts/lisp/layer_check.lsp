;;; layer_check.lsp
;;; LAYERCHECK - report layer counts for the active drawing.
;;; Prints total layers, locked layers and frozen layers.

(defun c:LAYERCHECK (/ layer name flags total locked frozen locked-names frozen-names)
  (setq total 0
        locked 0
        frozen 0
        locked-names '()
        frozen-names '())

  ;; Walk the layer table
  (setq layer (tblnext "LAYER" T))
  (while layer
    (setq name  (cdr (assoc 2 layer))
          flags (cdr (assoc 70 layer))
          total (1+ total))
    (if (= 4 (logand flags 4))
      (setq locked (1+ locked)
            locked-names (cons name locked-names)))
    (if (= 1 (logand flags 1))
      (setq frozen (1+ frozen)
            frozen-names (cons name frozen-names)))
    (setq layer (tblnext "LAYER")))

  (princ (strcat "\nTotal layers : " (itoa total)))
  (princ (strcat "\nLocked layers: " (itoa locked)))
  (foreach n (reverse locked-names) (princ (strcat "\n  - " n)))
  (princ (strcat "\nFrozen layers: " (itoa frozen)))
  (foreach n (reverse frozen-names) (princ (strcat "\n  - " n)))
  (princ)
)

(princ "\nLAYERCHECK loaded. Type LAYERCHECK to run.")
(princ)
