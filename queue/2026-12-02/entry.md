# Day 33 — 2026-12-02

## Topic: Daily Temperatures (Python)

**Problem:** Given daily temperatures, return for each day how many days you must wait until a warmer temperature — `[73, 74, 75, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`. Days that never get warmer are `0`.

## What I learned

- The naive way rescans forward from every day, which is O(n²); the stack turns it into one pass, because each day is pushed once and popped once.
- The stack is monotonic decreasing: it only ever holds days whose temperatures are in decreasing order, so the top is always the most recent day still waiting — and the first warmer day answers it.
- Equal temperatures do not count as warmer, so the pop condition is strictly `<`, not `<=` — a day at the same temperature keeps waiting, which is exactly what the `[70, 70, 71]` test checks.
- The answer for a day is a distance, not a temperature: when day `i` pops day `j`, the answer is `i - j`, and days left on the stack at the end keep their initial `0`.
- This is Day 7's Valid Parentheses idea grown up: there the stack matched openers with closers, here it matches cooler days with the warmer day that resolves them — same "unfinished work waits on the stack" shape, different question.

## Code

See [`daily_temperatures.py`](daily_temperatures.py) in this folder.

```python
def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # indices of days still waiting for a warmer day
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

## Example

`[73, 74, 75, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`. Strictly rising means every day waits 1; strictly falling means every day is `0`.

## Next

Day 34 topic to be chosen — the next batch after this refill.
