# Setup guide

## 1. Requirements

| Need | Why |
|---|---|
| Claude (Cowork app or Claude Code) | Runs the skills and automations |
| Claude in Chrome extension, signed in to your job sites | Searching and form filling happen in **your** browser session |
| Python 3.10+ with `openpyxl` and `pypdf` | Tracker builder and PDF checks (`pip install openpyxl pypdf`) |
| Optional: Gmail connector | Inbox watch and reply drafts |
| Optional: Slack connector | Notifications |

## 2. Install the privacy guard (do this first)

```bash
python3 scripts/install_hooks.py
```

This adds a git pre-commit hook that blocks any commit containing personal data or files from `my_data/`.

## 3. Load the skills

- **Claude app / Cowork**: add each folder in `skills/` as a skill (zip the folder if your app asks for a file).
- **Claude Code**: `mkdir -p .claude/skills && cp -r skills/* .claude/skills/`

## 4. Run the setup interview

Say: **"Run job-hunt-setup"**. Claude will ask about:

1. **Platforms**: which job sites to use (multi-select, or "all known platforms").
2. **Target roles**: job titles and keywords, and titles to exclude.
3. **Locations**: countries and cities, and whether remote is OK.
4. **Seniority and experience**: your years of experience, and the maximum years a posting may ask for.
5. **Salary**: current salary (or "Negotiable") and your expected-salary scheme per role type.
6. **Standard form answers**: notice period, nationality, relocation, sponsorship, and similar.
7. **Your CV**: the file to upload. Optionally, whether to generate tailored CVs per job.
8. **Approval mode**: stop at Review for every job (default), or auto-submit jobs you pre-approved.
9. **Consent policy**: whether Claude may tick required privacy-notice boxes for you.
10. **Notifications**: Slack, email or none.

It then writes these files (all git-ignored):

```
my_data/profile.md
my_data/preferences.yaml
my_data/form_answers.md
my_data/applied_log.json
my_data/cv/<your CV>.pdf      (you copy it here)
```

You can also fill them by hand: copy each `*.template.*` file from `config/` and `templates/` into `my_data/`, drop `.template` from the name, and replace every `[PLACEHOLDER]`.

## 5. First search

Say **"Run job-search"**. You get a shortlist table. Reply with the jobs to apply to, for example *"apply to 1, 3 and 5"*.

## 6. Scheduled automations (optional)

Open `automations/weekly_job_hunt.prompt.md`, copy the prompt into a new Claude scheduled task, and set the day and time.
Your computer and Chrome must be on and signed in when it runs, because it works through your browser.

## 7. Keeping your copy private

If you put your copy online, use a **private** repository. A public fork of a public repo cannot be made private.
The hook and CI scan protect you, but `my_data/` should never leave your machine.
