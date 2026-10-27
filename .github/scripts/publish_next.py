#!/usr/bin/env python3
"""Publish the next due daily-coding-log entry from the `queue` branch.

Reads queue entries from the `queue` branch (already fetched as
origin/queue), picks the earliest entry whose date has arrived in
Europe/London and that is not already on main, copies its log file and
code into YYYY/MM/ on main, and adds its row to the README log table.

Publishes at most ONE entry per run. If nothing is due, or the entry is
already on main, it writes its outputs and exits 0 without changing
any files, so the workflow makes no empty commit.

Outputs (to $GITHUB_OUTPUT, and printed for local runs):
  published_date  YYYY-MM-DD of the entry handled, or '' if none due
  day             Day number from meta.json
  topic           Topic from meta.json
  already_on_main 'true' if the entry was already published on main
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parents[2]
QUEUE_REF = "origin/queue"


def today_london() -> date:
    return __import__("datetime").datetime.now(ZoneInfo("Europe/London")).date()


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout


def git_show(ref_path: str) -> str:
    return git("show", ref_path)


def queue_dates() -> list[str]:
    """Sorted YYYY-MM-DD folder names under queue/ on the queue branch."""
    out = git("ls-tree", "-r", "--name-only", QUEUE_REF)
    dates = set()
    for line in out.splitlines():
        m = re.match(r"queue/(\d{4}-\d{2}-\d{2})/meta\.json$", line)
        if m:
            dates.add(m.group(1))
    return sorted(dates)


def read_meta(entry_date: str) -> dict:
    return json.loads(git_show(f"{QUEUE_REF}:queue/{entry_date}/meta.json"))


def update_readme(day: int, entry_date: str, topic: str) -> None:
    readme = REPO / "README.md"
    text = readme.read_text()
    row = f"| {day} | {entry_date} | {topic} |\n"
    if re.search(rf"^\| {day} \|", text, re.MULTILINE):
        print(f"README already has a Day {day} row, leaving it alone.")
        return
    lines = text.splitlines(keepends=True)
    # Insert into the Log table, keeping rows sorted by day number.
    table_start = next(
        i for i, line in enumerate(lines) if line.startswith("| Day | Date | Topic |")
    )
    insert_at = table_start + 2  # skip header + separator
    while insert_at < len(lines) and lines[insert_at].startswith("| "):
        m = re.match(r"\| (\d+) \|", lines[insert_at])
        if m and int(m.group(1)) < day:
            insert_at += 1
        else:
            break
    lines.insert(insert_at, row)
    readme.write_text("".join(lines))
    print(f"Added README row: {row.strip()}")


def set_output(name: str, value: str) -> None:
    print(f"{name}={value}")
    out_file = os.environ.get("GITHUB_OUTPUT")
    if out_file:
        with open(out_file, "a") as f:
            f.write(f"{name}={value}\n")


def main() -> int:
    today = today_london()
    print(f"Today (Europe/London): {today}")
    for entry_date in queue_dates():
        if date.fromisoformat(entry_date) > today:
            print(f"Stopping: {entry_date} is in the future.")
            break
        target = REPO / entry_date[:4] / entry_date[5:7] / f"{entry_date}.md"
        meta = read_meta(entry_date)
        day, topic = int(meta["day"]), meta["topic"]
        if target.exists():
            print(f"Day {day} ({entry_date}) is already on main; queue cleanup only.")
            set_output("published_date", entry_date)
            set_output("day", str(day))
            set_output("topic", topic)
            set_output("already_on_main", "true")
            return 0
        # Copy the entry and its code files into place.
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(git_show(f"{QUEUE_REF}:queue/{entry_date}/entry.md"))
        for code_file in meta.get("code_files", []):
            dest = target.parent / code_file
            dest.write_text(git_show(f"{QUEUE_REF}:queue/{entry_date}/{code_file}"))
            print(f"Wrote {dest.relative_to(REPO)}")
        update_readme(day, entry_date, topic)
        set_output("published_date", entry_date)
        set_output("day", str(day))
        set_output("topic", topic)
        set_output("already_on_main", "false")
        print(f"Ready to publish Day {day}: {topic} ({entry_date})")
        return 0
    print("Nothing due to publish.")
    set_output("published_date", "")
    set_output("day", "")
    set_output("topic", "")
    set_output("already_on_main", "false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
