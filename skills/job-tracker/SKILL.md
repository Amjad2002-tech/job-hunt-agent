---
name: job-tracker
description: Maintains the application log and rebuilds the Excel tracker with totals; imports an existing tracker; answers questions like "how many jobs have I applied to" or "list my applications". Use for "update my tracker", "job-tracker", "how many jobs did I apply to".
---

# Job tracker

## Source of truth
`my_data/applied_log.json`. The workbook is always rebuilt from it, never edited as the master.

## Rebuild
```
python3 scripts/build_tracker.py                 # writes my_data/generated/Job_Tracker.xlsx
python3 scripts/build_tracker.py --out PATH.xlsx
```
The workbook uses `templates/Job_Tracker.template.xlsx` (Job Applications + Summary sheets).

## Import an old tracker
Read the user's xlsx/csv, map columns (company, title, location, date, link, status), add each as a log entry with `platform: imported` and keep its status. De-duplicate on link or company + title.

## Reconcile with a platform
If the user asks "is this all?", pull the platform's own applied list (for example LinkedIn My Jobs > Applied, signed in), add any missing entries as `Applied`, and report what was added.

## Answers
Counts by status and platform, applications per week, reply rate, oldest open applications without a reply (follow-up candidates).
