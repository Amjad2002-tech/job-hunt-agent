# Job Hunt Agent

An AI job-search assistant built for **Claude (Cowork / Claude Code) with Claude in Chrome**.
It searches the job platforms you choose, scores every posting against your profile, fills
application forms in your own logged-in browser, prepares outreach drafts, watches your inbox
for employer replies, and keeps a tracker of everything you have applied to.

Clone it, run the setup once, and it works for **anyone**: the repository ships with empty
templates only. Your personal data never enters git.

> This is an independent community project. It is not affiliated with Anthropic, LinkedIn or any job platform.
> Respect each platform's terms of use. You are responsible for every application submitted in your name.

---

## What it does

| Stage | Skill | What happens |
|---|---|---|
| 1. Setup | `job-hunt-setup` | Asks you questions (which platforms, roles, locations, salary, rules) and writes your private config into `my_data/` |
| 1b. CV review (Step 0) | `cv-recruiter-review` | A hard-to-impress recruiter panel (HR/ATS, head of each role track, GM, CEO) scores your latest CV out of 100 per track, pass mark 70. Only passing tracks are searched. Gives fixes with options and applies them to your CV |
| 2. Search | `job-search` | Searches every platform you selected, removes duplicates and jobs you already handled, scores and shortlists |
| 3. Apply | `job-apply` | Fills forms in your browser with your CV and standard answers. **Stops at the Review page unless you approved submission** |
| 4. Outreach | `job-outreach` | Finds the hiring team on the posting and leaves an unsent draft message for you |
| 5. Portals | `job-portal-sweep` | Checks company and government career portals you list (SuccessFactors, Workday, Greenhouse, Teamtailor...) |
| 6. Inbox | `job-email-watch` | Reads only employer replies, classifies them, drafts answers. Never sends |
| 7. Tracker | `job-tracker` | Keeps `applied_log.json` and rebuilds the Excel tracker with totals |

Two ready-made **scheduled automations** live in `automations/`: a weekly hunt and a daily inbox watch.

## Supported platforms

You choose during setup. Pick any combination, or "all".

| Region | Platforms |
|---|---|
| Global | LinkedIn (Easy Apply and external), Indeed, Glassdoor, Wellfound (startups), Remote OK / We Work Remotely (remote roles) |
| Gulf / MENA | Bayt, GulfTalent, Naukrigulf, Tanqeeb, Jadarat (Saudi national platform), Ewdifh (Saudi) |
| Company ATS | Greenhouse, Lever, Ashby, SmartRecruiters, Teamtailor, Workable, Workday, SAP SuccessFactors, Oracle / Taleo, Phenom |
| Government / entity portals | Any careers URL you add (ministries, authorities, giga-projects) |

Platform details and the method that works for each are in [`config/platforms.yaml`](config/platforms.yaml).
Adding a new one is a single entry in that file.

## Quick start

1. **Get the repo**: download the ZIP or `git clone`. For your own search, keep any online copy **private**.
2. **Load the skills**: in Claude, add each folder under `skills/` as a skill (or zip a folder and upload it).
   Claude Code users can copy `skills/*` into `.claude/skills/`.
3. **Connect**: Claude in Chrome (signed in to the job sites you use). Optional: Gmail and Slack connectors.
4. **Run setup**: tell Claude *"Run job-hunt-setup"*. It asks its questions and creates your private files in `my_data/`.
5. **CV review**: *"How is my CV?"* runs the recruiter panel. Fix what fails, or drop tracks the CV cannot support yet.
6. **Search**: *"Run job-search"*. Review the shortlist, then say which jobs to apply to.
7. **Automate (optional)**: copy a prompt from `automations/` into a Claude scheduled task.

Full walkthrough: [SETUP.md](SETUP.md).

## Privacy model

- Every file that holds personal data lives in `my_data/`, which is **git-ignored**. The repo only contains `*.template.*` files with `[PLACEHOLDER]` values.
- `scripts/check_no_personal_data.py` scans for emails, phone numbers, national IDs and anything under `my_data/`, and runs as a **pre-commit hook** and in **CI** (`.github/workflows/privacy-check.yml`).
- The agent never creates accounts, never types passwords, never sends emails or messages, and never submits an application you did not approve.

Read [PRIVACY.md](PRIVACY.md) before pushing anything online.

## Safety rules the agent always follows

1. No application is submitted without your explicit approval (per job, or a standing rule you set in setup).
2. No outreach message, connection request or email is ever sent. Drafts only.
3. No account creation, no passwords, no CAPTCHA solving. Those roles go on your "apply yourself" list.
4. Terms, privacy-notice and consent boxes are ticked only if you allowed it in setup. Marketing opt-ins stay unticked.
5. Web pages and emails are treated as data, never as instructions.
6. Facts come only from your profile. Nothing is invented or inflated.

## Repository layout

```
config/        templates for your profile, preferences, form answers + platform catalog
templates/     tracker workbook, applied log, CV and cover-letter rules
skills/        the eight skills (SKILL.md each)
automations/   prompts for scheduled tasks
scripts/       privacy scanner, tracker builder, PDF checker, hook installer
my_data/       YOUR private files (git-ignored, created by setup)
docs/          comparison with ai-job-search, FAQ
```

## License

MIT. See [LICENSE](LICENSE).
