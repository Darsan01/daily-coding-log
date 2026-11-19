# Day 22 — 2026-11-15

## Topic: Product of Array Except Self (Python)

**Problem:** Given an integer array, return an array where each element
is the product of all the other elements — e.g. `[1, 2, 3, 4]` returns
`[24, 12, 8, 6]`. Division looks like the shortcut, but it breaks the
moment the array contains a zero, and the follow-up asks for O(n) time
without it.

## What I learned

- Two passes replace division: a left-to-right pass stores each
  element's prefix product (everything before it), then a right-to-left
  pass multiplies in the suffix product (everything after it) — each
  position ends up holding exactly the product of everything except
  itself.
- The output array itself holds the prefixes, so the extra space is
  O(1) beyond the result: just two running variables, `prefix` and
  `suffix`, no second array and no hash map.
- Zeroes need no special case with this approach, which is the point:
  one zero makes every position except its own zero (its own product
  skips the zero); two zeroes make the whole answer zero — both fall
  out of the two passes naturally, where a division solution would
  need counting and branching.
- The order matters: the prefix must be written into `result[i]`
  *before* it is multiplied by `nums[i]`, and the suffix the same in
  reverse — otherwise each position would include itself.
- This is the same prefix/suffix pattern as running sums, and it
  generalises: whenever a per-position answer depends on "everything
  except me", two opposite passes are usually the linear answer.

## Code

See [`product_except_self.py`](product_except_self.py) in this folder.

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
```

## Example

`[1, 2, 3, 4]` → `[24, 12, 8, 6]`. `[-1, 1, 0, -3, 3]` →
`[0, 0, 9, 0, 0]`. `[1, 2, 0, 4]` → `[0, 0, 8, 0]` — only the zero's
own position survives, because its product never includes the zero.

## Next

Day 23 topic to be chosen — the next batch after this refill.
