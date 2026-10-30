# Scheduled automations

Copy a prompt into a Claude scheduled task. Replace `[REPO_PATH]` with where the repo lives
(a connected folder on your computer, or a Claude Project that holds the same files).

| File | Suggested schedule | Needs |
|---|---|---|
| `weekly_job_hunt.prompt.md` | Once a week (for example Friday morning) | Chrome signed in, computer on |
| `daily_email_watch.prompt.md` | Daily | Gmail connector |
| `portal_sweep.prompt.md` | Weekly | Chrome; sign-in for portals that need it |

Scheduled runs are unattended: they never submit applications unless `approval.mode` is
`auto_submit_preapproved`, and never send messages or email.
