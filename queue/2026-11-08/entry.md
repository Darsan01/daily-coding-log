# Day 15 — 2026-11-08

## Topic: Climbing Stairs — Dynamic Programming (Python)
 (LeetCode 70)

**Problem:** You are climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top? E.g. `n = 3` → `3` ways (1+1+1, 1+2, 2+1).

## What I learned

- The last step is either a 1-step or a 2-step, so ways(n) = ways(n-1) + ways(n-2). That recurrence is Fibonacci in disguise — recognising a recurrence is half of every DP problem.
- Naive recursion recomputes the same subproblems exponentially (ways(30) calls itself millions of times). Memoisation — storing each answer the first time you compute it — drops that to linear, because each value from 0 to n is computed exactly once.
- You don't even need the table: only the previous two values matter, so two variables rolling forward give **O(n)** time and **O(1)** space. That's the bottom-up version in the code file.
- The pattern generalises: define the state, find the recurrence from the last decision, compute in an order where dependencies are already known, and keep only what the next step needs.

## Code

See [`climbing_stairs.py`](climbing_stairs.py) in this folder, with tests.

```python
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
```

## Example

`climb_stairs(2)` → `2`, `climb_stairs(3)` → `3`, `climb_stairs(5)` → `8`, `climb_stairs(45)` → `1836311903` (computed instantly, no recursion blow-up).

## Next

Best Time to Buy and Sell Stock: one pass, track the lowest price so far.
