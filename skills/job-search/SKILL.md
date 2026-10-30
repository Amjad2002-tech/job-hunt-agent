---
name: job-search
description: Searches the job platforms selected in my_data/preferences.yaml, removes duplicates and jobs already handled, scores postings against the user's profile and returns a ranked shortlist. Search only, never applies. Use for "find jobs", "search jobs", "job-search", or as step 1 of the weekly automation.
---

# Job search

## Inputs
`my_data/preferences.yaml`, `my_data/profile.md`, `my_data/applied_log.json`, `config/platforms.yaml`.
If preferences are missing, run `job-hunt-setup` first.

## Step 0. CV review gate
- Read `## Current track status` in `my_data/cv_review.md`. If the file is missing, or the CV in `my_data/cv/` (or the live CV page) is newer than the last review, run `cv-recruiter-review` Step 1 first.
- Search only the **passing** tracks, ranked with `best_fit` first. Use each track's keywords in scoring.
- If no track passes and `cv_review.block_search_if_no_track_passes` is true, stop and report the failing stage and reason, unless the user overrides in chat.

## Step 1. Plan the queries
- Tracks = the passing tracks from Step 0; target titles = `search.target_titles` that belong to those tracks (plus titles typical for each track).
- Platforms = `platforms.selected` (expand `all` to every entry in `config/platforms.yaml` that matches the user's countries).
- Queries = each target title, plus 2 to 4 broader terms built from `extra_keywords`.
- Window = `search.posted_within_days`.
- If the user said in chat "just checking" or "don't apply", this skill only reports.

## Step 2. Collect
For each platform, follow its `search` entry in `config/platforms.yaml`, in the user's signed-in Chrome:
- Throttle about one request every 2 to 3 seconds. On HTTP 429, "Failed to fetch" or a CAPTCHA: back off once, then skip that platform and report it.
- Large results: write them into the page (a `<pre>` element) and read with get_page_text.
- Record for each posting: platform, id, title, company, location, posted date, link.
- If a platform needs a sign-in the user has not done, record "not signed in" and move on.

## Step 3. Filter
Drop a posting when any of these is true:
- Its id or (company + title + platform) is already in `applied_log.json`.
- The signed-in page says it was already applied to (LinkedIn: "Application submitted").
- Title contains an `exclude_title_words` entry, or company is in `exclude_companies`.
- Program type is excluded (for example a one-time national training scheme the user already used).
- It asks for `max_years_required` or more years.
- Seniority is outside `candidate.seniority_levels_ok` (for example "Manager" when managers are excluded).
Keep duplicates across platforms once, preferring the source with the easiest apply method.

## Step 4. Score (0 to 100)
Fetch the description for the best ~40 candidates and score:
- 40 pts: keyword overlap with the profile skills and `extra_keywords`.
- 25 pts: title match with `target_titles`.
- 20 pts: experience fit (years asked vs `candidate.years_experience`).
- 15 pts: location, language and work-mode fit.
Write one **honest** fit note per job: why it fits and the main gap.

## Step 5. Shortlist
Top `search.shortlist_size`, with apply method detected (Easy Apply, company site + ATS name, email).
Mark company-site roles that need an account as **Apply yourself** (see `account: true` in platforms.yaml).

## Step 6. Output
- Table in chat: #, title, company, location, score, fit note, apply method, link.
- Append each shortlisted job to `my_data/applied_log.json` with status `Shortlisted`.
- Save a run note to `my_data/logs/search_<date>.md` (queries, counts per platform, blocked platforms).
- Ask which jobs to apply to, unless running inside an automation.
