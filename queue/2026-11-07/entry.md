# Day 14 — 2026-11-07

## Topic: Merge Two Sorted Lists (Python)
 (LeetCode 21)

**Problem:** Given the heads of two sorted linked lists, merge them into one sorted list and return its head. E.g. `1 → 2 → 4` and `1 → 3 → 4` become `1 → 1 → 2 → 3 → 4 → 4`.

## What I learned

- Walk both lists at once, always taking the smaller head — the same 'merge' step that mergesort uses. Because both inputs are sorted, the next element of the answer is always one of the two heads, so there is never a reason to look further ahead.
- A dummy head node removes all the special cases: without it, the first element needs separate handling; with it, every element — including the first — is just 'append to tail'. Return `dummy.next` at the end.
- Time: **O(n + m)** — every node is visited once. Space: **O(1)** — the nodes are re-linked, not copied. The recursive version is the same time but O(n + m) stack space, and it reads almost like the problem statement.
- Edge cases that must work: one list empty (answer is the other list), both empty (answer is None), and lists of different lengths (the leftover tail just gets attached whole).

## Code

See [`merge_two_lists.py`](merge_two_lists.py) in this folder, with tests.

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

## Example

`merge_two_lists(list_from([1, 2, 4]), list_from([1, 3, 4]))` → `[1, 1, 2, 3, 4, 4]`; merging with an empty list returns the other list unchanged.

## Next

Climbing Stairs: dynamic programming is just recursion with a notebook.
