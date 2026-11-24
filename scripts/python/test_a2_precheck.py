"""Offline tests for a2_precheck.py on a mock Plant 3D project (not real Plant 3D data).

Run: python3 -m unittest discover -s scripts/python -p 'test_*.py'
"""

import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import a2_precheck as pc  # noqa: E402

TOP = "A1 A2 Surname Firstname"


def make_db(path: Path, bad: bool) -> None:
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE Equipment (PnPID INTEGER, Tag TEXT)")
    eq = ["F-101", "F-102", "E-101", "P-301", "P-30?" if bad else "P-302"]
    con.executemany("INSERT INTO Equipment VALUES (?, ?)", enumerate(eq))
    con.execute("CREATE TABLE Nozzle (Tag TEXT, NominalDiameter REAL, PressureClass TEXT,"
                " EndType TEXT, Standard TEXT, NominalUnit TEXT)")
    con.executemany("INSERT INTO Nozzle VALUES (?,?,?,?,?,?)", [
        ("N1", 100.0, "10", "FL", "DIN 2632", "mm"),
        ("N2", 80.0, "150" if bad else "10", "FL", "DIN 2632", "mm"),
    ])
    con.execute("CREATE TABLE Pipe (LineNumberTag TEXT, Spec TEXT, NominalDiameter REAL)")
    con.executemany("INSERT INTO Pipe VALUES (?,?,?)", [
        ("150-10HC01-LPHW-1001", "10HC01", 150.0),
        ("" if bad else "100-10HC01-LPHW-1002", "10HC01", 100.0),
        ("80-10HC01-LPHW-1003", "10HS01" if bad else "10HC01", 80.0),
        ("25-10HC01-D-1004", "10HC01", 25.0),
    ])
    con.execute("CREATE TABLE Valve (Tag TEXT, LineNumberTag TEXT, Spec TEXT)")
    con.executemany("INSERT INTO Valve VALUES (?,?,?)", [
        ("HA-101", "100-10HC01-LPHW-1002", "10HC01"),
        ("HA-101" if bad else "HA-102", "100-10HC01-LPHW-1002", "10HC01"),
        ("V-?" if bad else "HA-103", "80-10HC01-LPHW-1003", "10HC01"),
    ])
    con.commit()
    con.close()


def make_zip(tmp: Path, bad: bool) -> Path:
    db = tmp / "Piping.dcf"
    make_db(db, bad)
    z = tmp / "project.zip"
    with zipfile.ZipFile(z, "w") as zf:
        zf.write(db, f"{TOP}/Piping.dcf")
        zf.writestr(f"{TOP}/Plant 3D Models/TC 3D Layout.dwg", b"x")
        if not bad:
            zf.writestr(f"{TOP}/Engineering Items.xlsx", b"x")
        zf.writestr("../evil.dcf", b"not sqlite")  # zip-slip entry must be ignored
    return z


class PrecheckTest(unittest.TestCase):
    def run_on(self, bad: bool) -> pc.Report:
        with tempfile.TemporaryDirectory() as t:
            return pc.run(make_zip(Path(t), bad))

    def test_good_project_passes(self):
        rep = self.run_on(bad=False)
        self.assertEqual(rep.fails, 0, "\n".join(rep.lines))
        text = "\n".join(rep.lines)
        self.assertIn("PASS        project folder name", text)
        self.assertIn("PASS        valve tags HA-1xx", text)
        self.assertIn("PASS        every pipe part has a line number", text)

    def test_bad_project_reports_each_problem(self):
        text = "\n".join(self.run_on(bad=True).lines)
        for expected in ("equipment tags without '?': ['P-30?']",
                         "missing ['P-302']",
                         "N2: class '150'",
                         "(1 without)",
                         "(1 other)",
                         "valve tags HA-1xx: ['V-?']",
                         "valve tags unique: ['HA-101']",
                         "FAIL        Engineering Items Excel"):
            self.assertIn(expected, text)

    def test_unknown_schema_is_cant_check_not_pass(self):
        with tempfile.TemporaryDirectory() as t:
            tmp = Path(t)
            con = sqlite3.connect(tmp / "Piping.dcf")
            con.execute("CREATE TABLE Something (a TEXT)")
            con.commit()
            con.close()
            rep = pc.run(tmp)
        text = "\n".join(rep.lines)
        self.assertIn("CAN'T CHECK equipment tags", text)
        self.assertIn("CAN'T CHECK valve tags", text)
        self.assertNotIn("PASS        valve", text)

    def test_schema_mode_lists_tables(self):
        with tempfile.TemporaryDirectory() as t:
            rep = pc.run(make_zip(Path(t), bad=False), show_schema=True)
        text = "\n".join(rep.lines)
        self.assertIn("Nozzle (2 rows): Tag, NominalDiameter", text)


if __name__ == "__main__":
    unittest.main()
