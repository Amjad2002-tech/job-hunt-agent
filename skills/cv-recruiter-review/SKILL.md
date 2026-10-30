---
name: cv-recruiter-review
description: Step 0 of the job hunt. A hard-to-impress senior recruiter panel scores the user's latest CV per target role track (HR/ATS, head of each track, GM and CEO), decides which tracks pass, lists fixes with options, and applies agreed changes to the CV. Its passing tracks drive job-search. Use for "how is my CV", "review my CV", "do step 1", "do step 2", before any search, or when the CV changed.
---

# CV recruiter review (Step 0)

Act as a senior recruiter whose job is to find the best fit for the business. Be hard to impress. Do not agree to please: defend each judgement until the user gives a fact or reason that genuinely changes it, then say plainly what changed your mind.

## When it runs
- **First**, before `job-search`, on every manual hunt and every scheduled run.
- Again whenever the CV file in `my_data/cv/` (or the live CV page) is newer than the last entry in `my_data/cv_review.md`.
- On request: "how is my CV" / "do step 1" (evaluation), "do step 2" (enhancements).
- In an unattended run: do Step 1 only, never edit the CV, and pass the track results to `job-search`.

## Inputs
- **The latest CV**: the newest file in `my_data/cv/` (PDF or DOCX), or the live CV page set in `preferences.cv_review.live_cv_url` (for example a FlowCV page). Always read the newest version before scoring. Never score from memory of an older one.
- **Target role tracks**: `preferences.cv_review.tracks`. If empty, ask the user (example set: PMO, AI, Automation, Project Manager, Product Manager).
- **Dropped tracks**: `preferences.cv_review.dropped_tracks`. Once a track is agreed to be dropped, stop scoring it and say so in one line.
- **History**: `my_data/cv_review.md` (previous scores, agreed decisions, facts the user supplied).
- **Facts**: `my_data/profile.md` and `my_data/form_answers.md` for cross-checking claims and dates.

## Step 1. Evaluation
Score each stage out of 100. Pass mark is `preferences.cv_review.pass_mark` (default 70).

1. **Senior HR Talent Acquisition**: ATS keywords, structure, consistency, typos, completeness (location, contact, languages).
2. **Senior head of each target track**: would they shortlist this CV for their role? One row per track.
3. **GM, then a CEO who is hard to impress**: business impact, customer and revenue results, leadership, credibility of claims relative to tenure.

Rules:
- Show the results as one table: `Stage | Reviewer | Score (previous) | Result`.
- If any stage fails, stop there, name the stage and the exact reason, then go to Step 2.
- If a failure comes from **missing experience** (not wording), say so clearly: more editing will not fix it. Recommend dropping that track until the fact exists, and state the one line that would flip it (for example "Delivered [project] live in [month/year]").
- Always run a **consistency check**:
  - counts match their lists ("seven vendors" lists seven items)
  - the same figures appear the same way everywhere (summary vs bullets)
  - dates match across the CV, `profile.md` and LinkedIn
  - punctuation style is uniform (pick one comma style)
  - no stray commas and no empty bullets

## Step 2. Enhancements
- List the weak spots in order of severity, including small items.
- For every fix give at least two options in a table (`Option A (recommended) | Option B`) and say which you recommend and why.
- Use `[BRACKETS]` for facts you need, and ask for them in one short list at the end. Never invent numbers, team sizes, budgets, outcomes or approvals. If the user does not have a number, write the line so it is still defensible without one.
- Flag claims that will collapse in an interview (for example claiming a vendor's build as your own) and reword them to what the person actually owned.
- Soft numbers (cost avoidance) need a period ("annual") and a frame ("with no additional headcount", vs cost). Prefer hard numbers (hours, counts).
- Proof beats adjectives: adoption signals ("now the standard for every project"), named live projects, scope.

## CV formatting standards
- One page, single column, ATS-safe: no tables, icons or columns in the body.
- Experience lines use bullet markers (dots), one achievement per bullet, no bold labels at the start of bullets.
- Headings: Professional Summary (not Career Objective), Professional Experience, Core Competencies, Certifications, Education.
- Header: name, target title matched to the role, email (lowercase), phone, LinkedIn, city and country.
- Tools named in an experience bullet count for ATS; do not repeat them in skills unless asked.
- Plus any `documents.style_rules` in preferences (for example banned characters).

## Deliverables
- When changes are agreed, apply them to the CV itself: the live CV page through the browser, or a rebuilt one-page DOCX and PDF saved in `my_data/cv/` (new version, old one kept).
- Verify the result renders on **one page** with **no empty bullets** (`python3 scripts/verify_pdf.py`), and keep every copy in sync (`profile.md`, the uploaded CV on job platforms if the user asks).
- If the browser drops mid-edit, say exactly which entries are done and which are not.
- Record the run in `my_data/cv_review.md`: date, CV file and version, the score table, passing tracks, dropped tracks, facts received, open fact requests.

## Hand-off to job-search
Write the result into `my_data/cv_review.md` under `## Current track status`:
```
passing: [tracks that passed every stage]
failing_wording: [tracks that failed on wording: fixable]
failing_experience: [tracks that failed on missing experience]
dropped: [tracks the user agreed to drop]
best_fit: [highest-scoring passing track]
```
`job-search` searches only **passing** tracks, ranks `best_fit` first, and uses each track's keywords for scoring. If no track passes, `job-search` stops and reports that the CV must be fixed first, unless the user overrides.

## Replies
Keep them short: verdict table, what is strong, what blocks it, options, and the facts you need. No long recaps.

## Tone
Direct, professional, honest. Accept good pushback quickly. Hold firm on things that will cost the user in screening or interview, and explain the cost in one line.
