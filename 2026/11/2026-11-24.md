# Day 25 — 2026-11-24

## Topic: Merge Intervals (Python)

**Problem:** Given intervals like `[[1, 3], [2, 6], [8, 10],
[15, 18]]`, merge every overlapping pair and return the disjoint
intervals covering the same ranges — `[[1, 6], [8, 10], [15, 18]]`.
It is the sorting-first pattern: sort, then one pass.

## What I learned

- Sorting by start is what makes one pass possible: after the sort,
  an interval can only overlap with the one before it, never with
  an earlier one — so there is no need to look backwards or restart.
- The merge test is a single comparison: if the next start is less
  than or equal to the current merged end, they overlap, and the new
  end is the larger of the two ends — using `max` handles the case
  where one interval sits entirely inside another.
- Touching intervals merge too (`[1, 4]` and `[4, 5]` become
  `[1, 5]`), because the test is `start <= merged end`, not
  `start < merged end` — a one-character difference that changes
  the answer, and the self-test pins it down.
- The input is copied before sorting (`sorted` returns a new list)
  and merged intervals are stored as fresh lists, so the caller's
  data is never mutated — the same care as Day 22, where the output
  array was built rather than overwriting the input.
- Cost is O(n log n) time, dominated by the sort, and O(n) space
  for the output — the pass itself is linear, which is why this
  pattern shows up wherever ranges need consolidating: calendars,
  meeting rooms, IP ranges.

## Code

See [`merge_intervals.py`](merge_intervals.py) in this folder.

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

## Example

`[[1, 3], [2, 6], [8, 10], [15, 18]]` → `[[1, 6], [8, 10],
[15, 18]]`. `[[1, 4], [4, 5]]` → `[[1, 5]]`. `[[1, 4], [2, 3]]`
→ `[[1, 4]]` — the inner interval disappears entirely.

## Next

Day 26 topic to be chosen — the next batch after this refill.
