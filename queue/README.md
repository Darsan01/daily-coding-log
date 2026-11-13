# Queue — pre-prepared daily entries

One folder per day, named by its publish date (`YYYY-MM-DD`).
Each folder holds:
- `meta.json` — day number, date, topic, code files
- `entry.md` — the dated log file to publish
- the code file(s), already written and tested

The GitHub Actions workflow on `main` (`.github/workflows/daily-publish.yml`)
publishes the earliest entry whose date has arrived, one per day, and
removes the published folder from this branch. Nothing here is live on
`main` until its date arrives.
