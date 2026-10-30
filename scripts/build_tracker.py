#!/usr/bin/env python3
"""Rebuild the Excel tracker from my_data/applied_log.json.

  python3 scripts/build_tracker.py [--log my_data/applied_log.json] [--out my_data/generated/Job_Tracker.xlsx]
"""
import argparse
import json
import pathlib
import shutil
import sys

from openpyxl import load_workbook

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "Job_Tracker.template.xlsx"
FIRST_ROW = 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=str(ROOT / "my_data" / "applied_log.json"))
    ap.add_argument("--out", default=str(ROOT / "my_data" / "generated" / "Job_Tracker.xlsx"))
    a = ap.parse_args()

    log_path = pathlib.Path(a.log)
    if not log_path.exists():
        sys.exit(f"No log at {log_path}. Run job-hunt-setup first.")
    entries = [e for e in json.loads(log_path.read_text(encoding="utf-8")) if not str(e.get("id", "")).startswith("[")]

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(TEMPLATE, out)
    wb = load_workbook(out)
    ws = wb["Job Applications"]
    for i, e in enumerate(entries):
        r = FIRST_ROW + i
        reply = e.get("reply")
        if isinstance(reply, dict):
            reply = f"{reply.get('date', '')} {reply.get('type', '')}".strip()
        values = [i + 1, e.get("platform"), e.get("company"), e.get("title"), e.get("location"),
                  e.get("posted"), e.get("score"), e.get("fit_note"), e.get("expected_salary"),
                  e.get("link"), e.get("apply_method"), e.get("status"), e.get("applied_on"),
                  "; ".join(x for x in [reply or "", e.get("open_question") or "", e.get("note") or ""] if x)]
        for c, v in enumerate(values, 1):
            ws.cell(r, c, v)
        if e.get("link"):
            ws.cell(r, 10).hyperlink = e["link"]
    wb.save(out)
    counts = {}
    for e in entries:
        counts[e.get("status", "?")] = counts.get(e.get("status", "?"), 0) + 1
    print(f"Tracker written: {out} ({len(entries)} jobs) {counts}")


if __name__ == "__main__":
    main()
