#!/usr/bin/env python3
"""Install a git pre-commit hook that runs the personal-data check."""
import os
import pathlib
import stat

ROOT = pathlib.Path(__file__).resolve().parent.parent
hooks = ROOT / ".git" / "hooks"
if not hooks.exists():
    raise SystemExit("No .git folder here. Run `git init` (or clone the repo) first.")
hook = hooks / "pre-commit"
hook.write_text("#!/bin/sh\npython3 scripts/check_no_personal_data.py || exit 1\n", encoding="utf-8")
hook.chmod(hook.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
print(f"Installed {hook.relative_to(ROOT)}")
