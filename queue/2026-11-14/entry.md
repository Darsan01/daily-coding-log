# Day 21 — 2026-11-14

## Topic: Top K Frequent Elements (Python)

**Problem:** Given an integer array and `k`, return the `k` most frequent
elements — e.g. `[1, 1, 1, 2, 2, 3]` with `k = 2` returns `[1, 2]`.
Sorting by frequency is the obvious first try, but it costs O(n log n);
there is a linear-time way.

## What I learned

- Counting first is the same hash-map move as Day 18 (Group Anagrams):
  one pass with `Counter` gives every element's frequency in O(n).
- Bucket sort by frequency is the key trick: frequencies range from 1
  to n, so an array of n + 1 buckets — bucket `f` holding every element
  that appears exactly `f` times — sorts by frequency without any
  comparison sort, in O(n) time and O(n) space.
- Walking the buckets from the top (highest frequency down) and
  collecting until `k` elements are found gives the answer; the walk
  stops early, so it never needs to scan buckets below the cut-off.
- The heap alternative (`heapq.nlargest`, O(n log k)) is shorter to
  write and fine for small inputs, but bucket sort is the linear
  answer interviewers expect for this problem — knowing both, and when
  each wins, is the point.
- Edge cases that matter: `k` equal to the number of distinct elements
  (return all of them), every element appearing once (any `k` of them
  is correct — order within the answer is not guaranteed), and a
  single-element array.

## Code

See [`top_k_frequent.py`](top_k_frequent.py) in this folder.

```python
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

## Example

`[1, 1, 1, 2, 2, 3]`, `k = 2` → `[1, 2]` (1 appears 3 times, 2 appears
twice). `[4, 4, 4, 4]`, `k = 1` → `[4]`. `[1, 2, 3]`, `k = 2` → any
two of the three, since all frequencies are 1.

## Next

Day 22 topic to be chosen — the next batch after this refill.
