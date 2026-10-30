---
name: job-hunt-setup
description: First-time setup for the Job Hunt Agent. Interviews the user (job platforms to use, target roles, locations, salary, form answers, approval and consent policy) and writes their private config into my_data/. Use when the user says "set up my job search", "job-hunt-setup", or when my_data/preferences.yaml is missing.
---

# Job hunt setup

Goal: create the user's private files in `my_data/` from the templates, asking only what is needed.
Nothing personal is written anywhere else.

## Step 0. Check existing state
- If `my_data/preferences.yaml` exists, read it and ask whether to **update** specific sections or **start over**.
- Never overwrite `my_data/applied_log.json` if it already has entries.

## Step 1. Platforms (always ask first)
Ask with a multi-select question (AskUserQuestion when available, otherwise a numbered list in chat):

> "Which job platforms should I search and apply on?"

Offer these groups (read the full catalog in `config/platforms.yaml`):
1. **All platforms I know** (recommended for the widest search)
2. **LinkedIn**
3. **Gulf / MENA boards**: Bayt, GulfTalent, Naukrigulf, Tanqeeb
4. **National platforms**: Jadarat and other government portals for the user's country
5. **Global boards**: Indeed, Glassdoor, Wellfound, remote boards
6. **Specific company or government careers pages** (ask for the URLs)

If the user picks "All", store `selected: [all]`. Then ask whether they are already **signed in** to each platform in Chrome; note the ones that are not, so runs can list them instead of failing.

## Step 2. Target
Ask in at most two rounds:
- Target job titles (3 to 15) and titles or words to exclude.
- Countries, cities, remote OK?
- Years of experience, and the maximum years a posting may ask for.
- Seniority levels that are acceptable (entry to executive).
- Include graduate programs? Exclude internships or specific programs?
- Companies to exclude (for example the current employer).

## Step 3. Profile
Offer three ways and use the one the user chooses:
1. **Read my CV**: the user drops their CV into `my_data/cv/`; extract facts into `config/profile.template.md` structure.
2. **Paste CV text** in chat.
3. **Interview**: ask role by role.
Then ask for 3 to 5 **proof points** they are happy to quote, and anything they must **never** claim.
Show the drafted `profile.md` and let them correct it before saving.

## Step 4. Form answers and salary
Walk through `config/form_answers.template.md`. For sensitive fields (date of birth, gender, marital status, relatives, criminal record, disability) let the user answer or choose **ASK** so runs come back to them.
Salary: current (or "Negotiable"), numeric fallback, expected scheme per role type, minimum acceptable.

## Step 5. Documents
- Which CV file to upload (must be inside `my_data/cv/`).
- Tailored CV per job: yes or no. Cover letter: none, generic or tailored.
- File-name stem and style rules (one page, banned characters...).

## Step 5b. Role tracks for the CV review
Ask which role tracks the CV should be judged for (3 to 6, for example PMO, AI, Automation, Project Manager, Product Manager), the pass mark (default 70), and the live CV page URL if they keep one. Store them under `cv_review` in preferences.

## Step 6. Policies
- **Approval mode**: `review_first` (default: stop at the Review page) or `auto_submit_preapproved` with explicit rules.
- **Consent policy**: `ask` (default) or `allow_required` (tick required privacy or terms boxes, never marketing).
- **Outreach** on or off, and tone (fill `config/outreach_style.template.md`).
- **Email watch** on or off. **Notifications**: none, Slack (user id), email, push.

## Step 7. Write files
Create, with every placeholder replaced:
- `my_data/preferences.yaml` (from `config/preferences.template.yaml`)
- `my_data/profile.md`, `my_data/form_answers.md`, `my_data/outreach_style.md`
- `my_data/applied_log.json` as `[]` if absent
- `my_data/.private_terms` with the user's full name, phone and email (one per line) so the privacy scanner blocks them
Then run `python3 scripts/check_no_personal_data.py --all` and confirm the repo outside `my_data/` is clean.

## Step 8. Import past applications (optional)
If the user has an old tracker (xlsx or csv), import rows into `applied_log.json` with status `Applied` so they are never shortlisted again.

## Finish
Summarise the settings in five lines, then run `cv-recruiter-review` Step 1 straight away (it is Step 0 of every hunt) and suggest "Run job-search" once at least one track passes.
