#!/usr/bin/env python3
"""A2 pre-submission check: read a zipped Plant 3D project (or its folder) and
report the lecturer's check-list items that live in the project database.

Usage:
    python3 a2_precheck.py "A1 A2 Surname Firstname.zip"
    python3 a2_precheck.py <project folder>
    python3 a2_precheck.py <zip or folder> --schema   # list tables/columns only

Read-only: the zip is never extracted to disk except the .dcf databases, which
are copied to a temporary folder and opened read-only. Standard library only.

The Plant 3D database layout is not documented publicly, so tables and columns
are found by name (e.g. a table called "Nozzle" or "Valve", a column called
"Tag" or "LineNumberTag"). Anything it cannot find is reported as CAN'T CHECK,
never as PASS. Each line starts with PASS, FAIL, WARN or CAN'T CHECK.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sqlite3
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

EXPECTED_EQUIPMENT = {"F-101", "F-102", "E-101", "P-301", "P-302"}
SPEC = "10HC01"
VALVE_TAG = re.compile(r"^HA-1\d\d$")
LINE_SIZES = {"25", "80", "100", "150"}
DRAWING = "TC 3D Layout.dwg"

TAG_COLS = ("Tag",)
LINE_COLS = ("LineNumberTag", "LineNumber", "LineTag")
SIZE_COLS = ("NominalDiameter", "Size", "NominalSize")
CLASS_COLS = ("PressureClass", "Rating")
END_COLS = ("EndType", "EndTypes", "Facing")
STD_COLS = ("Standard", "DesignStd", "DesignStandard")
UNIT_COLS = ("NominalUnit", "Units", "Unit")
SPEC_COLS = ("Spec", "PipeSpec")


@dataclass
class Report:
    lines: list[str] = field(default_factory=list)
    fails: int = 0

    def add(self, status: str, msg: str) -> None:
        if status == "FAIL":
            self.fails += 1
        self.lines.append(f"{status:11s} {msg}")


# ---------------------------------------------------------------- loading

def _safe_member(name: str) -> bool:
    p = PurePosixPath(name)
    return not p.is_absolute() and ".." not in p.parts


def collect(source: Path, workdir: Path) -> tuple[list[str], list[Path]]:
    """Return (all file names in the project, local copies of the .dcf files)."""
    names: list[str] = []
    dcfs: list[Path] = []
    if source.is_dir():
        for p in sorted(source.rglob("*")):
            if p.is_file():
                rel = p.relative_to(source).as_posix()
                names.append(rel)
                if p.suffix.lower() == ".dcf":
                    dst = workdir / f"{len(dcfs)}_{p.name}"
                    shutil.copyfile(p, dst)
                    dcfs.append(dst)
    else:
        with zipfile.ZipFile(source) as zf:
            for info in zf.infolist():
                if info.is_dir() or not _safe_member(info.filename):
                    continue
                names.append(info.filename)
                if info.filename.lower().endswith(".dcf"):
                    dst = workdir / f"{len(dcfs)}_{PurePosixPath(info.filename).name}"
                    with zf.open(info) as fh, dst.open("wb") as out:
                        shutil.copyfileobj(fh, out)
                    dcfs.append(dst)
    return names, dcfs


def open_ro(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def schema(con: sqlite3.Connection) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for (name,) in con.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        cols = [r[1] for r in con.execute(f'PRAGMA table_info("{name}")')]
        out[name] = cols
    return out


def pick(cols: list[str], wanted: tuple[str, ...]) -> str | None:
    low = {c.lower(): c for c in cols}
    for w in wanted:
        if w.lower() in low:
            return low[w.lower()]
    return None


def rows(con: sqlite3.Connection, table: str, cols: list[str]) -> list[dict]:
    sel = ", ".join(f'"{c}"' for c in cols)
    cur = con.execute(f'SELECT {sel} FROM "{table}"')
    return [dict(zip(cols, r)) for r in cur]


def tables_like(sch: dict[str, list[str]], *words: str) -> list[str]:
    return [t for t in sch if any(w.lower() == t.lower() for w in words)]


def txt(v) -> str:
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


# ----------------------------------------------------------------- checks

def check_files(names: list[str], rep: Report) -> None:
    tops = {n.split("/")[0] for n in names if "/" in n}
    if len(tops) == 1:
        top = next(iter(tops))
        ok = re.fullmatch(r"A1 A2 \S+ \S+", top) or re.fullmatch(r"A2 \S+ \S+", top)
        rep.add("PASS" if ok else "WARN", f"project folder name: {top!r}")
    else:
        rep.add("CAN'T CHECK", "project folder name (zip has no single top folder)")
    dwgs = [n for n in names if PurePosixPath(n).name.lower() == DRAWING.lower()]
    rep.add("PASS" if dwgs else "FAIL", f"drawing {DRAWING!r} in project" +
            (f" ({dwgs[0]})" if dwgs else ""))
    if not any(PurePosixPath(n).name.lower() == "piping.dcf" for n in names):
        rep.add("FAIL", "Piping.dcf not found: zip the whole project folder")
    xls = [n for n in names if n.lower().endswith((".xls", ".xlsx"))]
    rep.add("PASS" if xls else "FAIL",
            "Engineering Items Excel in project folder" + (f" ({xls[0]})" if xls else ""))


def check_equipment(con, sch, rep: Report) -> None:
    tabs = tables_like(sch, "Equipment")
    if not tabs:
        rep.add("CAN'T CHECK", "equipment tags (no Equipment table)")
        return
    tags: set[str] = set()
    for t in tabs:
        c = pick(sch[t], TAG_COLS)
        if c:
            tags |= {txt(r[c]) for r in rows(con, t, [c])}
    bad = sorted(x for x in tags if "?" in x or not x)
    missing = sorted(EXPECTED_EQUIPMENT - tags)
    rep.add("FAIL" if bad else "PASS", "equipment tags without '?'" + (f": {bad}" if bad else ""))
    rep.add("FAIL" if missing else "PASS",
            "equipment F-101, F-102, E-101, P-301, P-302 present" +
            (f"; missing {missing}" if missing else ""))


def check_nozzles(con, sch, rep: Report) -> None:
    tabs = tables_like(sch, "Nozzle")
    if not tabs:
        rep.add("CAN'T CHECK", "nozzle size/class/end/standard (no Nozzle table)")
        return
    for t in tabs:
        cols = sch[t]
        got = {k: pick(cols, v) for k, v in
               (("tag", TAG_COLS), ("size", SIZE_COLS), ("cls", CLASS_COLS),
                ("end", END_COLS), ("std", STD_COLS), ("unit", UNIT_COLS))}
        use = [c for c in got.values() if c]
        if not use:
            rep.add("CAN'T CHECK", f"nozzles: table {t} has none of the expected columns")
            continue
        data = rows(con, t, use)
        rep.add("PASS" if data else "FAIL", f"nozzles found: {len(data)}")
        probs = []
        for i, r in enumerate(data, 1):
            name = txt(r.get(got["tag"])) if got["tag"] else f"#{i}"
            if got["size"] and txt(r[got["size"]]) not in {"80", "100"}:
                probs.append(f"{name}: size {txt(r[got['size']])!r}")
            if got["cls"] and "10" not in txt(r[got["cls"]]):
                probs.append(f"{name}: class {txt(r[got['cls']])!r}")
            if got["end"] and "FL" not in txt(r[got["end"]]).upper():
                probs.append(f"{name}: end {txt(r[got['end']])!r}")
            if got["std"] and "2632" not in txt(r[got["std"]]):
                probs.append(f"{name}: standard {txt(r[got['std']])!r}")
            if got["unit"] and txt(r[got["unit"]]).lower() not in {"mm", ""}:
                probs.append(f"{name}: unit {txt(r[got['unit']])!r}")
        rep.add("FAIL" if probs else "PASS",
                "nozzles 80/100 mm, FL, class 10, DIN 2632" + (": " + "; ".join(probs) if probs else ""))
        for k, label in (("cls", "class"), ("end", "end type"), ("std", "standard")):
            if not got[k]:
                rep.add("CAN'T CHECK", f"nozzle {label} (no column found)")


def check_piping(con, sch, rep: Report) -> None:
    tabs = tables_like(sch, "Pipe", "Valve", "Fitting", "Flange", "Elbow", "Tee",
                       "Reducer", "Instrument", "InlineInstrument", "Olet", "Cap")
    if not tabs:
        rep.add("CAN'T CHECK", "line numbers and spec (no Pipe/Valve/Fitting tables)")
        return
    no_line = specs_bad = 0
    sizes: set[str] = set()
    checked_line = checked_spec = False
    for t in tabs:
        cols = sch[t]
        lc, sc, zc = pick(cols, LINE_COLS), pick(cols, SPEC_COLS), pick(cols, SIZE_COLS)
        use = [c for c in (lc, sc, zc) if c]
        if not use:
            continue
        for r in rows(con, t, use):
            if lc:
                checked_line = True
                v = txt(r[lc])
                if not v or "?" in v:
                    no_line += 1
            if sc:
                checked_spec = True
                if txt(r[sc]) and txt(r[sc]).upper() != SPEC:
                    specs_bad += 1
            if zc and t.lower() == "pipe":
                sizes.add(txt(r[zc]))
    if checked_line:
        rep.add("FAIL" if no_line else "PASS",
                "every pipe part has a line number" + (f" ({no_line} without)" if no_line else ""))
    else:
        rep.add("CAN'T CHECK", "line numbers (no LineNumberTag column)")
    if checked_spec:
        rep.add("FAIL" if specs_bad else "PASS",
                f"all parts in spec {SPEC}" + (f" ({specs_bad} other)" if specs_bad else ""))
    else:
        rep.add("CAN'T CHECK", "spec (no Spec column)")
    if sizes:
        missing = sorted(LINE_SIZES - sizes, key=int)
        extra = sorted(sizes - LINE_SIZES)
        msg = f"pipe sizes in model: {sorted(sizes)}"
        if missing:
            msg += f"; none yet at {missing}"
        if extra:
            msg += f"; unexpected {extra}"
        rep.add("WARN" if (missing or extra) else "PASS", msg)


def check_valves(con, sch, rep: Report) -> None:
    tabs = tables_like(sch, "Valve")
    if not tabs:
        rep.add("CAN'T CHECK", "valve tags (no Valve table)")
        return
    tags: list[str] = []
    for t in tabs:
        c = pick(sch[t], TAG_COLS)
        if c:
            tags += [txt(r[c]) for r in rows(con, t, [c])]
    bad = [x or "(blank)" for x in tags if not VALVE_TAG.match(x)]
    dup = sorted({x for x in tags if x and tags.count(x) > 1})
    rep.add("PASS" if tags else "FAIL", f"valves found: {len(tags)}")
    if tags:
        rep.add("FAIL" if bad else "PASS", "valve tags HA-1xx" + (f": {bad}" if bad else ""))
        rep.add("FAIL" if dup else "PASS", "valve tags unique" + (f": {dup}" if dup else ""))


def run(source: Path, show_schema: bool = False) -> Report:
    rep = Report()
    with tempfile.TemporaryDirectory() as tmp:
        names, dcfs = collect(source, Path(tmp))
        if not show_schema:
            check_files(names, rep)
        piping = [d for d in dcfs if d.name.lower().endswith("piping.dcf")]
        for d in (dcfs if show_schema else piping[:1]):
            con = open_ro(d)
            try:
                sch = schema(con)
                if show_schema:
                    rep.lines.append(f"== {d.name.split('_', 1)[1]}: {len(sch)} tables")
                    for t in sorted(sch):
                        n = con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
                        rep.lines.append(f"{t} ({n} rows): {', '.join(sch[t])}")
                    continue
                check_equipment(con, sch, rep)
                check_nozzles(con, sch, rep)
                check_piping(con, sch, rep)
                check_valves(con, sch, rep)
            finally:
                con.close()
    if not show_schema:
        rep.add("CAN'T CHECK", "open ports, head heights, supports, steel: check in Plant 3D")
    return rep


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("source", type=Path, help="zipped project or project folder")
    ap.add_argument("--schema", action="store_true", help="list database tables and columns")
    a = ap.parse_args(argv)
    if not a.source.exists():
        print(f"not found: {a.source}", file=sys.stderr)
        return 2
    rep = run(a.source, a.schema)
    print("\n".join(rep.lines))
    if not a.schema:
        print(f"\n{rep.fails} FAIL")
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
