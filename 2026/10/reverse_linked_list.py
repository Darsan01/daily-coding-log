"""Day 6 — Reverse a Linked List (LeetCode 206).

Given the head of a singly linked list, reverse it and return the new head.
1 -> 2 -> 3 -> 4 -> 5 becomes 5 -> 4 -> 3 -> 2 -> 1.

Approach (iterative): walk the list with three pointers — prev, current,
next_node. At each step save next_node first (otherwise the rest of the
list is lost), point current.next at prev, then advance both pointers.

Time:  O(n). Space: O(1) for the iterative version.
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def reverse_list(head: "ListNode | None") -> "ListNode | None":
    """Reverse the list iteratively and return the new head."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def reverse_list_recursive(head: "ListNode | None") -> "ListNode | None":
    """Reverse the list recursively (same result, O(n) stack space)."""
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    passed = 0
    for values, expected in cases:
        got = list_to_values(reverse_list(list_from(values)))
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: reverse_list({values}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
        got_rec = list_to_values(reverse_list_recursive(list_from(values)))
        assert got_rec == expected, f"recursive failed on {values}"
    print("PASS: recursive version agrees on all cases")
    passed += 1
    print(f"\n{passed}/{len(cases) + 1} tests passed")
    assert passed == len(cases) + 1, "some tests failed"


if __name__ == "__main__":
    _run_tests()
