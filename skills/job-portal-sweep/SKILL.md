---
name: job-portal-sweep
description: Checks the company and government careers portals listed in preferences.platforms.company_portals (SuccessFactors, Workday, Talentera, Greenhouse, Teamtailor and others) for new openings that match the user's targets, and applies where no account is needed and the user approved. Use for "check the careers page of X", "search ministry jobs", "job-portal-sweep".
---

# Job portal sweep

## Inputs
`preferences.platforms.company_portals` (name + URL), plus any portal the user names in chat. `config/platforms.yaml` for ATS methods.

## For each portal
1. Open the URL in the user's Chrome. If it fails (DNS error, page not found), search the web for the entity's current careers page once, then report.
2. Detect the ATS from the URL (see `detect` in platforms.yaml) and use its listing method or public API.
3. List every opening: title, location, posting date, closing date, reference number, link.
4. Mark matches against `target_titles` and filters. A portal with "no jobs" is a valid result: report it.
5. Also check the entity's LinkedIn company Jobs tab when useful.

## Applying on portals
- Only if the user approved applying to these jobs.
- If the portal needs an account and the user is **not** signed in: stop, list as `Apply yourself`, and say what to do ("sign in, then tell me").
- If the user **is** signed in: fill job-specific questions from `form_answers.md`, keep their profile values, never change national ID fields, never enter passwords.
- Profile fields shared across all jobs on that portal (current title, CV) can be updated once if the user agreed.
- Verify each submission by the portal's confirmation text.

## Output
Table per portal: opening, match yes/no, status. Update `applied_log.json` with `platform: company_site` and the portal's reference number in `note`.
