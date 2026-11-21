# Day 24 — Invert Binary Tree (Python).
# Swap every node's left and right children, recursively.
# The classic tree-recursion shape: handle this node, then recurse
# on both children. A queue-based iterative version does the same
# work level by level.
# Self-test (no network): python3 invert_binary_tree.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def to_list(root):
    """Level-order list, trailing Nones trimmed — for testing only."""
    if root is None:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [4,2,7,1,3,6,9]",
          to_list(invert_tree(from_list([4, 2, 7, 1, 3, 6, 9]))),
          [4, 7, 2, 9, 6, 3, 1])

    # 2. Two levels.
    check("two levels [2,1,3]",
          to_list(invert_tree(from_list([2, 1, 3]))), [2, 3, 1])

    # 3. Empty tree stays empty.
    check("empty", to_list(invert_tree(None)), [])

    # 4. Single node is unchanged.
    check("single node [1]",
          to_list(invert_tree(from_list([1]))), [1])

    # 5. Left-only chain becomes right-only.
    check("left chain [1,2]",
          to_list(invert_tree(from_list([1, 2]))), [1, None, 2])

    # 6. Inverting twice restores the original.
    tree = from_list([4, 2, 7, 1, 3, 6, 9])
    invert_tree(invert_tree(tree))
    check("double invert restores",
          to_list(tree), [4, 2, 7, 1, 3, 6, 9])

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
