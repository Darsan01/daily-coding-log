# Day 26 — Maximum Depth of Binary Tree (Python).
# Depth is 1 + the deeper of the two subtrees; an empty tree is 0.
# Same recursion shape as Day 24's invert: handle this node, then
# recurse on both children — here combining their answers instead
# of swapping them.
# Self-test (no network): python3 max_depth.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


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
    check("example [3,9,20,None,None,15,7]",
          max_depth(from_list([3, 9, 20, None, None, 15, 7])), 3)
    # 2. Right-leaning chain.
    check("right chain [1,None,2]", max_depth(from_list([1, None, 2])), 2)
    # 3. Balanced three nodes.
    check("balanced [1,2,3]", max_depth(from_list([1, 2, 3])), 2)
    # 4. Left-leaning, depth 3.
    check("left depth [1,2,3,4]", max_depth(from_list([1, 2, 3, 4])), 3)
    # 5. Empty tree is depth 0.
    check("empty", max_depth(None), 0)
    # 6. Single node is depth 1.
    check("single node [1]", max_depth(from_list([1])), 1)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
