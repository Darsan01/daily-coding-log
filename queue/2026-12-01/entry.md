# Day 32 — 2026-12-01

## Topic: Kth Largest Element in an Array (Python)

**Problem:** Given an unsorted list of numbers and `k`, return the kth largest element — `[3, 2, 1, 5, 6, 4]`, `k = 2` → `5`. Duplicates count separately.

## What I learned

- Sorting the whole list works but does more than the question asks: the answer only needs the k biggest values, not a fully ordered list, so a heap of size `k` is the right-sized tool.
- A min-heap of size `k` holds exactly the k largest values seen so far — every new number either joins (and pushes the smallest of the k out) or is smaller than all of them and is ignored.
- The heap's root is the answer, not an intermediate: once all numbers have been seen, the smallest value in that heap of k largest values is, by definition, the kth largest overall.
- `heapq` in Python is a min-heap only, which is exactly what this needs — pushing and popping the smallest is the operation, and there is no need for a max-heap or a custom comparator.
- Cost is O(n log k) time and O(k) extra space, which beats sorting's O(n log n) when `k` is small — the same "keep only what matters" shape as Day 21's Top K Frequent Elements, with a heap instead of a counter.

## Code

See [`kth_largest.py`](kth_largest.py) in this folder.

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

## Example

`[3, 2, 1, 5, 6, 4]`, `k = 2` → `5`. `[3, 2, 3, 1, 2, 4, 5, 5, 6]`, `k = 4` → `4`. `k = 1` is the maximum, `k = len(nums)` is the minimum.

## Next

Day 33 topic to be chosen — the next batch after this refill.
