# Day 35 — 2026-12-04

## Topic: Rotate Array (Python)

**Problem:** Rotate a list right by `k` steps, in place — `[1, 2, 3, 4, 5, 6, 7]`, `k = 3` → `[5, 6, 7, 1, 2, 3, 4]`.

## What I learned

- Rotating by `k` is the same as cutting the list after `n - k` and swapping the two halves — and three reversals do exactly that swap without extra storage.
- The trick is the order: reverse the whole list first, then reverse the first `k` elements, then reverse the rest. Each reversal fixes one half into place.
- `k` must be reduced with `k %= n` first — rotating by `n` is a full turn, so `k = 4` on a 3-element list is the same as `k = 1`, which is what the second test checks.
- Reversing a slice in place needs care: `nums[:k] = reversed(nums[:k])` works because the right-hand side is consumed before assignment; assigning a reversed view of the same list directly would not.
- Cost is O(n) time and O(1) extra space — the same "rearrange in place" shape as Day 22's Product of Array Except Self, which also avoided a second array.

## Code

See [`rotate_array.py`](rotate_array.py) in this folder.

```python
def rotate(nums, k):
    n = len(nums)
    if n <= 1:
        return nums
    k %= n
    if k == 0:
        return nums
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
```

## Example

`[1, 2, 3, 4, 5, 6, 7]`, `k = 3` → `[5, 6, 7, 1, 2, 3, 4]`. `k = 0` or `k = n` leaves the list unchanged. `[-1, -100, 3, 99]`, `k = 2` → `[3, 99, -1, -100]`.

## Next

Day 36 topic to be chosen — the next batch after this refill.
