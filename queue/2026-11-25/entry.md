# Day 26 — 2026-11-25

## Topic: Maximum Depth of Binary Tree (Python)

**Problem:** Given a binary tree, find its maximum depth — the number of nodes on the longest path from the root down to a leaf. `[3, 9, 20, null, null, 15, 7]` has depth 3.

## What I learned

- Depth is defined recursively: the depth of a tree is 1 plus the deeper of its two subtrees, and an empty tree has depth 0 — that base case is what stops the recursion.
- This is the same recursion shape as Day 24's invert: handle this node, then recurse on both children. The difference is what comes back — invert swaps and returns the node, depth combines the two answers with `max`.
- A left-leaning or right-leaning chain shows why depth is about the longest path, not the number of nodes: `[1, null, 2]` has 2 nodes and depth 2, while a balanced `[1, 2, 3]` has 3 nodes and depth 2.
- The iterative version (a queue, counting levels) does the same work — O(n) time either way, since every node is visited once. Recursion costs O(depth) stack space; the queue version costs O(width).
- The `from_list` helper is reused from Day 24, so the tree built from a level-order list is the same shape the self-test expects.

## Code

See [`max_depth.py`](max_depth.py) in this folder.

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

## Example

`[3, 9, 20, null, null, 15, 7]` → `3`. `[1, null, 2]` → `2`. `[1, 2, 3]` → `2`. An empty tree → `0`, and a single node → `1`.

## Next

Day 27 topic to be chosen — the next batch after this refill.
