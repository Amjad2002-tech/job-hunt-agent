---
name: job-apply
description: Fills job application forms (LinkedIn Easy Apply, job boards, and no-account company ATS forms) in the user's signed-in Chrome, using their CV and standard answers. Stops at the Review page unless the user approved submission. Use for "apply to these jobs", "job-apply", or after job-search when the user picks jobs.
---

# Job apply

## Inputs
`my_data/preferences.yaml`, `my_data/form_answers.md`, `my_data/profile.md`, `my_data/applied_log.json`, `config/platforms.yaml`.

## Approval gate (check before every job)
- **Submit allowed** only when the user approved this job in chat, or `approval.mode: auto_submit_preapproved` and the job matches every `auto_submit_rules` entry.
- Otherwise fill everything, stop at the Review page, save the draft, status `Draft saved`.
- A request like "search only" or "don't apply" means no form is opened at all.

## Hard stops (save draft, ask the user, never guess)
- The site needs an account, a password, a one-time code, a national digital ID login or a CAPTCHA: status `Apply yourself`.
- A required consent or terms box, when `consent_policy` is `ask`.
- A question whose answer in `form_answers.md` is `ASK` or missing and is a judgement call (salary below `minimum_acceptable`, relatives, criminal record, health, past employment at the company).
- The CV upload would send a file outside `my_data/cv/` or `my_data/generated/`.

## Per platform
Follow the platform's `apply` entry in `config/platforms.yaml`. General method:
1. Open the job page (navigate, then wait for it to settle).
2. Start the apply flow (Easy Apply button, or the company ATS link, which may open a new tab).
3. Contact page: confirm name, email, phone match `form_answers.md`.
4. Resume: select or upload `documents.cv_file` (or the tailored CV for this job). Confirm the selected file name.
5. Questions: answer from `form_answers.md`. Numeric-only field: use the numeric fallback. Text fields: form_input; radio buttons: a real click. Scope dropdown options to the current list.
6. Expected salary: first matching rule in `salary.expected_scheme`.
7. Untick "follow company" and every marketing opt-in.
8. Reach Review. Re-read every answer. Then either stop (draft) or submit if approved.
9. After submit, verify (reload the job page and look for the platform's confirmation text). Only a verified submission becomes `Applied`.

## Recording
For each job update `my_data/applied_log.json`: status, applied_on, apply_method, expected_salary, and `open_question` when stopped.
Run `python3 scripts/build_tracker.py` at the end.

## Report
Counts first: submitted, drafts saved, apply yourself, skipped. Then each open question with the job it belongs to.
