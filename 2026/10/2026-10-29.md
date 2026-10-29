# Day 5 — 2026-10-29

## Topic: Binary Search (Python)
 (LeetCode 704)

**Problem:** Given a sorted array `nums` and a target, return the index of `target`, or `-1` if it is not present. E.g. `binary_search([-1, 0, 3, 5, 9, 12], 9)` → `4`.

## What I learned

- Every step throws away half the remaining array — that halving is why the cost is **O(log n)**, not O(n). For a million items that's about 20 comparisons instead of a million.
- The bug everyone writes once: `mid = (left + right) // 2` can overflow in languages with fixed-size integers. The safe form is `mid = left + (right - left) // 2`. Python ints don't overflow, but the habit is worth keeping.
- Loop invariant that keeps it correct: the answer, if it exists, is always inside `[left, right]`. `left = mid + 1` and `right = mid - 1` are safe because `mid` itself has just been checked and ruled out.
- The same skeleton finds more than an exact match — with a small tweak it finds the first element `>= target` (lower bound), which is the basis of `bisect` and of searching in rotated arrays.

## Code

See [`binary_search.py`](binary_search.py) in this folder, with tests.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Example

`binary_search([-1, 0, 3, 5, 9, 12], 9)` → `4`, `binary_search([-1, 0, 3, 5, 9, 12], 2)` → `-1`.

## Next

Reverse a Linked List: flip each node's pointer as you walk the list — O(1) space.
