---
name: job-outreach
description: Finds the hiring team or relevant recruiters on a job posting and prepares an unsent LinkedIn message, connection note or email draft for each, in the user's approved style. Never sends anything. Use for "draft outreach", "message the hiring manager", "job-outreach".
---

# Job outreach (drafts only)

## Inputs
`my_data/outreach_style.md`, `my_data/profile.md` (proof points), `my_data/applied_log.json`, `preferences.outreach`.

## Find the contact
1. Open the job page signed in and read the rendered text.
2. Use "Meet the hiring team" first. Then "People you can reach out to": keep only people at the hiring company in HR, recruiting, talent acquisition or the department that owns the role.
3. A school alum in an unrelated job is a "warm contact, not a hirer": use only if nobody better exists, and label it.
4. At most `outreach.max_people_per_job`. If none: record "no contact found". Never guess a person or an email address.
5. Skip people already drafted for in `applied_log.json`.

## Draft
- Follow `my_data/outreach_style.md` exactly (greeting, length, tone, sign-off, banned words).
- Name the exact job title and company. Use one or two proof points from the profile only.
- One clear ask. Say "I have applied" only if the log shows a verified submission; otherwise "I am applying".
- Connection notes: count characters and stay within the platform limit (LinkedIn: 200 for a note).

## Place the draft (never send)
- Connected or open profile: open Message, type the draft, leave the tab open.
- Not connected: Connect, Add a note, type the note, leave it open. Never click the final Send.
- Only InMail or Premium offered: do not use credits; put the text in the report as "no box available".
- An HR email printed on the posting: create an email **draft** only.
- Never press Enter in a message box. Open at most about 10 tabs per run, with pauses.

## Record
Add to the job's `outreach` list in `applied_log.json`: person, role, why chosen, profile link without query string, draft text, status (`draft in tab, not sent` / `no box available` / `no contact found`).
