#!/usr/bin/env python3
"""Summarise a bom.csv: total quantity grouped by (Category, Size_mm, Unit)."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def summarise(path: Path) -> dict[tuple[str, str, str], float]:
    totals: dict[tuple[str, str, str], float] = defaultdict(float)
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        required = {"Category", "Size_mm", "Qty", "Unit"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing column(s): {', '.join(sorted(missing))}")
        for line_no, row in enumerate(reader, start=2):
            try:
                qty = float(row["Qty"])
            except (TypeError, ValueError):
                print(f"warning: line {line_no}: invalid Qty {row['Qty']!r}, skipped",
                      file=sys.stderr)
                continue
            key = (row["Category"].strip(), row["Size_mm"].strip(), row["Unit"].strip())
            totals[key] += qty
    return totals


def fmt_qty(value: float) -> str:
    return str(int(value)) if value == int(value) else f"{value:g}"


def print_table(totals: dict[tuple[str, str, str], float]) -> None:
    headers = ("Category", "Size_mm", "Unit", "Total Qty")
    rows = [(c, s, u, fmt_qty(q)) for (c, s, u), q in sorted(totals.items())]
    widths = [max(len(h), *(len(r[i]) for r in rows)) if rows else len(h)
              for i, h in enumerate(headers)]
    line = "  ".join("{:<{w}}".format(h, w=w) for h, w in zip(headers, widths))
    print(line)
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print("  ".join("{:<{w}}".format(v, w=w) for v, w in zip(r, widths)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bom", type=Path, help="path to bom.csv")
    args = parser.parse_args()

    if not args.bom.is_file():
        parser.error(f"file not found: {args.bom}")
    try:
        totals = summarise(args.bom)
    except ValueError as exc:
        parser.error(str(exc))
    print_table(totals)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
