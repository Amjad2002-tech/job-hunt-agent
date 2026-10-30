# Privacy

## Where your data lives

| Data | Location | In git? |
|---|---|---|
| Name, contacts, career history | `my_data/profile.md` | No (ignored) |
| Salary, preferences, platforms | `my_data/preferences.yaml` | No |
| Standard form answers (date of birth, nationality, notice...) | `my_data/form_answers.md` | No |
| Every job handled, statuses, replies | `my_data/applied_log.json` | No |
| CV, cover letters, tracker workbook | `my_data/cv/`, `my_data/generated/` | No |
| Templates with placeholders only | `config/*.template.*`, `templates/` | Yes |

## Three layers of protection

1. **`.gitignore`** excludes `my_data/`, every PDF, DOCX and XLSX outside `templates/`, `.env` files and screenshots.
2. **Pre-commit hook** (`scripts/install_hooks.py`) runs `scripts/check_no_personal_data.py` on staged files and blocks the commit if it finds:
   - any path under `my_data/`
   - email addresses (other than `example.com` / `noreply` placeholders)
   - phone numbers in international or local mobile formats
   - 10-digit national ID or iqama numbers, and IBANs
   - names you list in `my_data/.private_terms` (one per line)
3. **CI** (`.github/workflows/privacy-check.yml`) runs the same scan on every push and pull request.

## What the agent never stores in the repo

Claude is instructed (see `CLAUDE.md`) to write personal data only into `my_data/` and never into skills, templates or docs.
If you improve a skill, check it with `python3 scripts/check_no_personal_data.py --all` before you commit.

## Sharing improvements

Generic improvements (a new platform entry, a better scoring rule) are welcome. Strip any personal example first.
