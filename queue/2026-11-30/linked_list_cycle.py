# Day 31 — Linked List Cycle (Python).
# Floyd's tortoise and hare: a fast pointer laps a slow one
# exactly when the list loops back on itself.
# Self-test (no network): python3 linked_list_cycle.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def build(values, pos):
    """Build a list from values; if pos >= 0, the tail links back
    to the node at index pos, making a cycle."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example: tail links back to index 1.
    check("cycle [3,2,0,-4] pos 1", has_cycle(build([3, 2, 0, -4], 1)), True)
    # 2. Two nodes looping back to the head.
    check("cycle [1,2] pos 0", has_cycle(build([1, 2], 0)), True)
    # 3. No cycle.
    check("no cycle [1] pos -1", has_cycle(build([1], -1)), False)
    # 4. Empty list has no cycle.
    check("empty []", has_cycle(build([], -1)), False)
    # 5. A single node pointing at itself.
    check("self-loop [1] pos 0", has_cycle(build([1], 0)), True)
    # 6. Longer straight list, no cycle.
    check("no cycle [1,2,3,4] pos -1", has_cycle(build([1, 2, 3, 4], -1)), False)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
