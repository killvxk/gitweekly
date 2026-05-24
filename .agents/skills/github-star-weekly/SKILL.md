---
name: github-star-weekly
description: Generate or update weekly markdown reports from a GitHub username's starred repositories and optional fork events. Use when the user asks to check GitHub stars, GitHub starred repos, starred weekly reports, 每周 star 周报, GitHub star/fork weekly, or wants to input a GitHub username and append only the weekly/ report without touching README/source files.
---

# GitHub Star Weekly

Generate a weekly report section from a GitHub user's starred repositories. The GitHub username is an input, not a hardcoded value: pass it as a positional argument, pass `--username`, type it at the prompt, or pipe it on stdin. Optionally include public fork events. This skill is designed for the `E:\gitweekly` repo style: write only `weekly/weekly-<start>_<end>.md`, reuse `links_cache/descriptions_cache.json`, and do not update README/source markdown unless the user explicitly asks.

## Quick command

Use PowerShell with UTF-8 output. Replace `<github_user>` with the requested account:

```powershell
$env:PYTHONIOENCODING='utf-8'
python .agents/skills/github-star-weekly/scripts/github_star_weekly.py <github_user> --write
```

Equivalent username input styles:

```powershell
python .agents/skills/github-star-weekly/scripts/github_star_weekly.py --username <github_user> --write
python .agents/skills/github-star-weekly/scripts/github_star_weekly.py --write       # prompts: GitHub username:
"<github_user>" | python .agents/skills/github-star-weekly/scripts/github_star_weekly.py --write
```

Include fork events only when requested:

```powershell
python .agents/skills/github-star-weekly/scripts/github_star_weekly.py <github_user> --include-forks --write
```

Useful options:

- `--date YYYY-MM-DD`: choose the week containing this local date.
- `--week-start YYYY-MM-DD --week-end YYYY-MM-DD`: force a Monday-Sunday style range.
- `--timezone Asia/Taipei`: timezone for week boundaries; default is `Asia/Taipei`.
- `--dry-run`: preview rows without writing.
- `--update-cache`: write generated descriptions back to `links_cache/descriptions_cache.json`.
- `--username <github_user>`: set the GitHub username explicitly; overrides the positional value.
- `--token-env GITHUB_TOKEN`: use a GitHub token from an environment variable for rate limit.

## Workflow

1. Inspect `git status --short` before editing. Do not overwrite unrelated user changes.
2. Run the script with the requested GitHub username.
3. Verify only `weekly/weekly-<start>_<end>.md` changed unless the user asked for cache updates.
4. Review generated descriptions. If a row is English, vague, or too long, refine it manually using the existing `auto-weekly` description style: concise Chinese, 15-25-ish characters when practical, no empty adjectives.
5. Run a quick validation:
   - The target weekly file exists.
   - The `GitHub Stars（<start> ~ <end>）` section appears once.
   - Re-running the same command is idempotent and adds no duplicate URLs.
6. Do not commit or push unless the user explicitly asks.

## Output layout

Append sections to the target weekly file:

```markdown
## GitHub Stars（2026-05-18 ~ 2026-05-24）

| 链接 | 描述 |
|------|------|
| [repo](https://github.com/owner/repo) | 中文描述 |
```

Optional forks section:

```markdown
## GitHub Forks（2026-05-18 ~ 2026-05-24）
```

The script de-duplicates URLs across the whole weekly file, so existing rows in normal `README.md`/`tools.md` sections will not be repeated in the star section.

## Notes

- GitHub's starred API needs `Accept: application/vnd.github.star+json` to return `starred_at` timestamps.
- Public fork discovery uses the GitHub public events API, which is recent-event limited. It is reliable for current-week runs but may be incomplete for old weeks.
- If GitHub rate limits anonymous requests, set `$env:GITHUB_TOKEN` and rerun.
