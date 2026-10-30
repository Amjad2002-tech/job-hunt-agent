# FAQ

**Will it apply without asking me?**
No, not by default. `approval.mode: review_first` fills forms up to the Review page and stops. You approve jobs in chat, or set `auto_submit_preapproved` with rules you choose.

**Why does it skip some company websites?**
Sites such as Workday or SuccessFactors need an account and password. The agent never creates accounts or types passwords, so those jobs go on your "Apply yourself" list. If you sign in first, it can fill the rest.

**Can I add a job board that is not listed?**
Yes. Add an entry to `config/platforms.yaml` with its search URL and apply notes, then select it in `my_data/preferences.yaml`.

**Is my data safe if I push the repo?**
`my_data/` is ignored, the pre-commit hook blocks personal data, and CI scans every push. Still, keep your own copy private.

**Does it work without Chrome?**
Searching and applying need Claude in Chrome. The email watch and tracker work without it.
