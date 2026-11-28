# Day 36 — 2026-12-05

## Topic: Min Stack (Python)

**Problem:** A stack with `push`, `pop`, `top` and `get_min` — every operation in O(1), including the minimum of everything currently in the stack.

## What I learned

- A plain stack forgets the minimum the moment it is popped, so each entry has to carry its own answer: store `(value, min-so-far)` pairs, and the minimum is always the second item of the top pair.
- Pushing is the only place the minimum is computed — `min(val, previous min)` — so `get_min` is just a read, never a scan, which is why the whole structure stays O(1).
- Popping needs no repair work at all: removing the top pair uncovers the pair below it, which already recorded the minimum of everything beneath it.
- Duplicate minimums are handled for free: pushing `2` twice stores `(2, 2)` twice, so popping one still leaves the other as the minimum, which the third test checks.
- Cost is O(1) time per operation and O(n) space for the pairs — the same "pay a little memory to keep a question instant" trade as Day 21's Top K Frequent Elements, which kept counts alongside values.

## Code

See [`min_stack.py`](min_stack.py) in this folder.

```python
class MinStack:
    def __init__(self):
        self.stack = []  # each item: (value, min-so-far)

    def push(self, val):
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]
```

## Example

Push `-2`, `0`, `-3` → `get_min()` is `-3`. Pop once → `top()` is `0`, `get_min()` is `-2`.

## Next

Day 37 topic to be chosen — the next batch after this refill.
