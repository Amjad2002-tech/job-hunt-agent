#!/usr/bin/env python3
"""Check generated CVs and cover letters: page count and banned characters.

  python3 scripts/verify_pdf.py FILE.pdf [--pages 1] [--banned "—–"]
"""
import argparse
import sys

from pypdf import PdfReader


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--banned", default="—–")
    a = ap.parse_args()
    bad = 0
    for f in a.files:
        reader = PdfReader(f)
        text = "".join(p.extract_text() or "" for p in reader.pages)
        found = sorted({ch for ch in text if ch in a.banned})
        ok = len(reader.pages) <= a.pages and not found
        bad += not ok
        print(f"{'OK  ' if ok else 'FAIL'} {f}: {len(reader.pages)} page(s), banned characters {found or 'none'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
