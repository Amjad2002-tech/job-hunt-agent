#!/usr/bin/env python3
"""Block personal data from entering git.

Usage:
  python3 scripts/check_no_personal_data.py            # scan files staged for commit
  python3 scripts/check_no_personal_data.py --all      # scan every tracked/untracked file outside my_data/
  python3 scripts/check_no_personal_data.py FILE...    # scan given files

Exit code 1 if anything is found.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRIVATE_DIR = "my_data/"
ALLOWED_IN_PRIVATE = {"my_data/README.md", "my_data/cv/.gitkeep",
                      "my_data/generated/.gitkeep", "my_data/logs/.gitkeep"}
SKIP_SUFFIXES = {".xlsx", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip"}
SELF = "scripts/check_no_personal_data.py"

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_OK = re.compile(r"@(example\.(com|org)|users\.noreply\.github\.com|anthropic\.com)$", re.I)
PHONE = re.compile(r"(?<![\w/])(\+\d{1,3}[\s-]?\d[\d\s-]{7,13}\d|\b05\d{8}\b)")
NATIONAL_ID = re.compile(r"\b[12]\d{9}\b")          # 10-digit national / residency ids
IBAN = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")


def private_terms():
    f = ROOT / "my_data" / ".private_terms"
    if not f.exists():
        return []
    return [t.strip() for t in f.read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")]


def staged_files():
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
                         cwd=ROOT, capture_output=True, text=True)
    return [l for l in out.stdout.splitlines() if l]


def all_files():
    files = []
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if p.is_file() and not rel.startswith((".git/", PRIVATE_DIR)) and "__pycache__" not in rel:
            files.append(rel)
    return files


def scan(rel, terms):
    problems = []
    if rel.startswith(PRIVATE_DIR) and rel not in ALLOWED_IN_PRIVATE:
        return [f"{rel}: file is inside my_data/ (private)"]
    path = ROOT / rel
    if rel == SELF or path.suffix.lower() in SKIP_SUFFIXES or not path.exists():
        return problems
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return problems
    for n, line in enumerate(text.splitlines(), 1):
        for m in EMAIL.finditer(line):
            if not EMAIL_OK.search(m.group(0)) and "[" not in line[max(0, m.start() - 1):m.start()]:
                problems.append(f"{rel}:{n}: email address '{m.group(0)}'")
        for rx, label in ((PHONE, "phone number"), (NATIONAL_ID, "10-digit ID number"), (IBAN, "IBAN")):
            for m in rx.finditer(line):
                problems.append(f"{rel}:{n}: {label} '{m.group(0).strip()}'")
        low = line.lower()
        for t in terms:
            if t.lower() in low:
                problems.append(f"{rel}:{n}: private term '{t}'")
    return problems


def main(argv):
    if "--all" in argv:
        files = all_files()
    elif len(argv) > 1:
        files = argv[1:]
    else:
        files = staged_files()
    terms = private_terms()
    problems = [p for f in files for p in scan(f, terms)]
    if problems:
        print("Personal data check FAILED. Remove these before committing:")
        for p in problems:
            print("  - " + p)
        return 1
    print(f"Personal data check passed ({len(files)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
