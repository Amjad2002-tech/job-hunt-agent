# Job Hunt Agent vs ai-job-search

Reference: [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) (MIT, Claude Code based).
Both are built on Claude and both keep personal data out of git. They solve different halves of the problem.

## In one line each
- **ai-job-search**: a *document factory*. Finds postings, scores fit, and writes a high-quality tailored CV and cover letter with a drafter and reviewer agent. You submit the application yourself.
- **Job Hunt Agent**: an *application operator*. Works inside your signed-in browser across many platforms: fills and (with approval) submits forms, drafts outreach, watches your inbox, keeps the tracker, and runs on a schedule.

## Feature comparison

| Area | ai-job-search | Job Hunt Agent (this repo) |
|---|---|---|
| Runs in | Claude Code CLI (terminal) | Claude Cowork app or Claude Code, with Claude in Chrome |
| Setup | `/setup` from documents, pasted CV or interview | `job-hunt-setup` interview, **asks which platforms to use** |
| Platform choice | Fixed portal skills, mostly **Danish** boards plus LinkedIn and Freehire; `/add-portal` generates new ones | User picks per profile: LinkedIn, Bayt, GulfTalent, Naukrigulf, Tanqeeb, Jadarat, Indeed, Glassdoor, Wellfound, remote boards, any company or government portal |
| Search method | Bun/TypeScript CLIs per portal, with tests | In-browser fetch and page reading via Claude in Chrome; methods documented in `config/platforms.yaml` |
| CV quality gate | Drafter + reviewer agents per application | **`cv-recruiter-review` (Step 0)**: HR/ATS, head-of-track, GM and CEO panel scores the master CV per track, pass mark 70, consistency check, fixes with options; only passing tracks are searched |
| Fit scoring | Five-dimension framework, `/rank` batch scoring with parallel agents | 100-point score (keywords, title, experience, location) plus honest fit note |
| CV / cover letter | **Strong**: LaTeX templates, drafter + reviewer agents, ATS parse check, page-count check | Optional: use your own CV as-is (default) or generate tailored PDFs; page and character checks |
| Filling application forms | Writes text for you to paste (`08-application-forms.md`) | **Fills the form in your browser** (Easy Apply, Bayt, Greenhouse, Teamtailor, SuccessFactors when signed in...) |
| Submitting | Never: you submit | Stops at Review by default; submits only jobs you approved, verified by the site's confirmation |
| Account-only portals | Not covered | Detected and listed as "Apply yourself"; never creates accounts or types passwords |
| Outreach to hiring team | Not covered | Finds the hiring team, leaves unsent LinkedIn notes or email drafts |
| Email | `/gmail-sync` proposes status updates | `job-email-watch` classifies replies, updates the log, drafts replies, notifies |
| Interview prep | **`/interview`** prep pack and mock interview | Not yet (planned) |
| Salary data | `salary_lookup.py` with union/survey data | Expected-salary scheme per role type set in setup |
| Tracker | CSV + offline HTML dashboard, Notion sync | JSON log + Excel workbook with summary sheet |
| Scheduling | Manual commands | Ready prompts for weekly hunt, daily inbox watch, portal sweep |
| Prompt-injection defence | Deterministic posting guard (hidden text, invisible characters) | Instruction-level: pages and emails are data only |
| Privacy | `.gitignore` + docs warning that forks are public | `my_data/` ignored + **pre-commit scanner** + **CI scan** for emails, phones, IDs, IBANs, your own names |
| Tests / CI | Large pytest and bun test suite | Privacy CI; scripts are small and self-checking |
| Regions | Denmark first, methodology country-agnostic | Gulf / MENA first, global boards included |

## Where ai-job-search is stronger
1. Per-application document generation: LaTeX templates and an ATS parse check on every tailored CV and cover letter. (Our Step 0 review closes much of the gap on the master CV, but theirs reviews each tailored document.)
2. Interview preparation and outcome tracking (`/interview`, `/outcome`).
3. Prompt-injection defence that runs as code before the model reads a posting.
4. Engineering maturity: tests, versioned methodology files, upstream update tooling.

## Where Job Hunt Agent is stronger
1. It actually applies: form filling in your session, with an approval gate.
2. Platform choice at setup and Gulf / MENA coverage, including government portals.
3. Outreach drafts and inbox watch with reply drafts.
4. Scheduled, unattended runs with clear hard rules.
5. Automatic privacy scanning before commit and in CI, not only `.gitignore`.
6. A recruiter-panel CV gate that decides which role tracks are worth searching at all, and says when a track fails on missing experience rather than wording.

## Ideas worth borrowing next
- A deterministic posting guard script (strip hidden text and invisible characters before scoring).
- A reviewer pass on generated CVs (second agent checks every claim against the profile).
- An `interview` skill using the archived posting and the CV actually sent.
- An HTML dashboard from `applied_log.json`.
