"""Day 14 — Merge Two Sorted Lists (LeetCode 21).

Given the heads of two sorted linked lists, merge them into one sorted
list and return its head.

Approach: walk both lists at once, always taking the smaller head.
A dummy head node removes the special case for the first element.

Time:  O(n + m). Space: O(1) — nodes are re-linked, not copied.
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def merge_two_lists(l1: "ListNode | None", l2: "ListNode | None") -> "ListNode | None":
    """Merge two sorted lists iteratively and return the new head."""
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


def list_from(values: list[int]) -> "ListNode | None":
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def list_to_values(head: "ListNode | None") -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def _run_tests() -> None:
    cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [1, 2], [1, 2, 5]),
        ([1, 1, 1], [2, 2], [1, 1, 1, 2, 2]),
    ]
    passed = 0
    for a, b, expected in cases:
        got = list_to_values(merge_two_lists(list_from(a), list_from(b)))
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: merge({a}, {b}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
