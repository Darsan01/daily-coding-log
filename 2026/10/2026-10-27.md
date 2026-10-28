# Day 3 — 2026-10-27

## Topic: Maximum Subarray (Kadane's algorithm) (Python)
 (LeetCode 53)

**Problem:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) with the largest sum, and return that sum. E.g. `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → `6` (from `[4, -1, 2, 1]`).

## What I learned

- This is the "one pass, two running numbers" pattern: `current_sum` tracks the best subarray **ending at this position**, and `best_sum` tracks the best subarray seen **anywhere so far**.
- At each number the only decision is: extend the running subarray (`current_sum + x`) or start fresh at `x`. Take whichever is larger — a running sum that has gone negative can never help a future subarray, so dropping it is always safe.
- The all-negative edge case matters: the answer is then the single least negative element (e.g. `[-1, -2, -3]` → `-1`), not zero — the subarray must contain at least one number. Initialising both sums to `nums[0]` instead of `0` handles this naturally.
- Compared to the brute-force O(n²) check of every subarray, Kadane's is a single pass. Time: **O(n)**. Space: **O(1)** — just the two running values.
- Bonus in the code file: a version that also returns the subarray's start and end indices, which needs one extra "where did this run start" tracker.

## Code

See [`max_subarray.py`](max_subarray.py) in this folder, with tests.

```python
def max_subarray(nums):
    current_sum = best_sum = nums[0]
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

## Example

`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` → `6`, and `max_subarray([5, 4, -1, 7, 8])` → `23`.

## Next

Two Pointers — Valid Palindrome: one pointer at each end, moving inward.
