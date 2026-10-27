# Day 6 — 2026-10-30

## Topic: Reverse a Linked List (Python)
 (LeetCode 206)

**Problem:** Given the head of a singly linked list, reverse the list and return the new head. E.g. `1 → 2 → 3 → 4 → 5` becomes `5 → 4 → 3 → 2 → 1`.

## What I learned

- Three pointers do it in one pass: `prev`, `current`, and a saved `next_node`. The order of operations is everything — save `next` first, or the rest of the list is lost the moment you re-point `current.next`.
- Iterative reversal is **O(n)** time and **O(1)** space. The recursive version is the same time but O(n) stack space, and it reads more elegantly once you see that reversing the tail and then fixing the last link is the whole job.
- The `None` cases are the real test: an empty list and a one-node list both reverse to themselves, and the code handles them with no special case because the loop simply never runs / runs once.
- This pattern — walk a list while re-pointing as you go — is the core of most linked-list problems: cycle detection, merging two sorted lists, removing the nth node from the end.

## Code

See [`reverse_linked_list.py`](reverse_linked_list.py) in this folder, with tests.

```python
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

## Example

`reverse_list(list_from([1, 2, 3, 4, 5]))` → `5 → 4 → 3 → 2 → 1`; `reverse_list(None)` → `None`.

## Next

Stack — Valid Parentheses: push openers, pop on closers, and the stack must end empty.
