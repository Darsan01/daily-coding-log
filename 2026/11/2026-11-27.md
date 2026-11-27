# Day 28 — 2026-11-27

## Topic: 3Sum (Python)

**Problem:** Given an integer array, return all unique triplets `[a, b, c]` with `a + b + c == 0`. Each triplet is listed once, in non-decreasing order — e.g. `[-1, 0, 1, 2, -1, -4]` → `[[-1, -1, 2], [-1, 0, 1]]`.

## What I learned

- Sorting first turns a three-way search into a one-plus-two-pointer problem: fix the first number, then run two pointers (one at each end of the rest) to find pairs that sum to its negative. That is O(n²) instead of the O(n³) brute force of trying every triplet.
- Skipping duplicates is the whole difficulty, not the search: after sorting, equal values sit next to each other, so the first number is skipped if it equals the previous one, and after a hit both pointers skip past equal values. Without that, `[-1, -1, 2]` would appear twice.
- This is Day 1's Two Sum grown up: Two Sum used a hash map for one complement; here the sorted order plus two pointers replaces the map, because the target changes for every first element and the pair must be found in order.
- The two-pointer move rule follows from the sort: if the sum is too small, the left pointer moves right to a larger value; if too large, the right pointer moves left. Every step discards a pair that cannot work, so the inner scan is a single pass.
- Early exit: once the fixed first number is positive, no triplet starting there can sum to zero (the other two are at least as large), so the loop can stop — a small win that falls out of the sort for free.

## Code

See [`three_sum.py`](three_sum.py) in this folder.

```python
def three_sum(nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```

## Example

`[-1, 0, 1, 2, -1, -4]` → `[[-1, -1, 2], [-1, 0, 1]]`. `[0, 0, 0]` → `[[0, 0, 0]]`. `[1, 2, 3]` → `[]` (no triplet sums to zero). `[0, 1, 1]` → `[]`.

## Next

Day 29 topic to be chosen — the next batch after this refill.
