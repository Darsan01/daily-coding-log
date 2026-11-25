# Day 31 — 2026-11-30

## Topic: Linked List Cycle (Python)

**Problem:** Given the head of a linked list, return `True` if any node can be reached again by following `next` pointers — that is, the list contains a cycle — and `False` otherwise. `[3, 2, 0, -4]` with the tail linked back to the node holding `2` → `True`.

## What I learned

- Two pointers at different speeds settle this without any extra storage: the slow pointer moves one node at a time, the fast pointer two, and if there is a cycle the fast one laps the slow one and they meet — exactly like two runners on a circular track.
- The meeting test is identity, not value: `slow is fast` checks that both pointers are the same node object. Two different nodes can hold the same value, so comparing values would give false positives.
- The loop guard is the safety net: `fast is not None and fast.next is not None` must be checked before every double step, because the fast pointer is the one that can run off the end of a list with no cycle.
- A cycle does not have to include the head — in the textbook example the loop starts at the second node, and the pointers still meet inside it, because once the slow pointer enters the loop the fast one is already circling it.
- This is Day 6's Reverse Linked List from the other side: reversing rewired the pointers, here they are only read — and the same `ListNode` shape carries both, which is why the helper for building a test list (with an optional tail link back) is the part worth getting right.

## Code

See [`linked_list_cycle.py`](linked_list_cycle.py) in this folder.

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## Example

`[3, 2, 0, -4]` with the tail linked back to `2` → `True`. `[1, 2]` linked back to `1` → `True`. `[1]` with no link → `False`, and a single node pointing at itself → `True`.

## Next

Day 32 topic to be chosen — the next batch after this refill.
