# Day 23 — 2026-11-22

## Topic: Container With Most Water (Python)

**Problem:** Given heights of vertical lines, pick two lines that, with the x-axis, form a container holding the most water. `[1,8,6,2,5,4,8,3,7]` holds 49.

## What I learned

- The brute force is every pair — O(n²). The two-pointer move is the insight: start at the widest pair, then move the shorter side inward, because only a taller line can beat the current area.
- Area is width × the shorter height, so the shorter side is always the limiting factor — moving the taller side can never help.
- This is the same two-pointer shape as Day 4's Valid Palindrome, applied to an optimisation problem instead of a yes/no check.
- Two edge cases: a single line (or none) holds 0 — there is no container — and equal heights, where either side can move.

## Code

See [`container_with_most_water.py`](container_with_most_water.py) in this folder.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

## Example

`[1,8,6,2,5,4,8,3,7]` → `49`. `[1,1]` → `1`. `[4,3,2,1,4]` → `16`.

## Next

Day 24 topic to be chosen — the next batch after this refill.
