# CV and cover-letter rules

Applied only when `documents.tailor_cv_per_job` or `documents.cover_letter` is switched on in preferences.

## Grounding
- Every line must come from `my_data/profile.md`. Reorder and select; never invent or inflate.
- Respect "Things I must NEVER claim" in the profile.

## Tailoring
- Pick the 5 to 7 profile achievements that best match the posting's keywords.
- Mirror the posting's wording for skills you really have (helps ATS matching).
- Keep job titles, employers and dates exactly as in the profile.

## Format (defaults, override in preferences.documents.style_rules)
- One page, single column, standard fonts, no tables or text boxes (ATS-safe).
- File names: `{file_name_stem}.pdf` and `{file_name_stem}_Cover_Letter.pdf`. No company name in the file name.
- Verify every PDF with `python3 scripts/verify_pdf.py <file>` (page count and banned characters).

## Cover letter
- 180 to 250 words, three short paragraphs: why this role, two proof points, one clear close.
- Same tone rules as `my_data/outreach_style.md`.
