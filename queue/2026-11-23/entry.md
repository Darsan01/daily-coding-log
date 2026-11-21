# Day 24 — 2026-11-23

## Topic: Invert Binary Tree (Python)

**Problem:** Swap every node's left and right children, so the
mirror image of the tree comes out — `[4, 2, 7, 1, 3, 6, 9]`
becomes `[4, 7, 2, 9, 6, 3, 1]`. It is the textbook first tree
recursion problem, and the shape of the solution is the shape of
most tree problems that follow.

## What I learned

- The recursion is two lines once the base case is set: if the node
  is `None`, return `None`; otherwise swap the children, recursing
  into each. The swap must happen on the *results* of the recursive
  calls — swapping first and then recursing into the swapped
  children works too, but only if you recurse into the new children.
- Python's tuple assignment makes the swap one line:
  `root.left, root.right = invert_tree(root.right),
  invert_tree(root.left)` — both recursive calls are evaluated
  before either assignment lands, so nothing is lost.
- Inverting twice restores the original tree, which is a neat
  self-check: it proves the operation is its own inverse, and it
  caught a wrong-swap bug in an early draft of the test.
- The iterative version (a queue, swapping each node as it is
  visited) does the same work level by level — same O(n) time, O(n)
  space in the worst case either way, since every node is visited
  once and the queue/stack holds at most one level.
- Level-order lists are only a testing convenience here: the
  `to_list` / `from_list` helpers turn a tree into a flat list so
  the self-test can compare values directly.

## Code

See [`invert_binary_tree.py`](invert_binary_tree.py) in this folder.

```python
def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

## Example

`[4, 2, 7, 1, 3, 6, 9]` → `[4, 7, 2, 9, 6, 3, 1]`. `[2, 1, 3]` →
`[2, 3, 1]`. An empty tree stays empty, and a single node is
unchanged.

## Next

Day 25 topic to be chosen — the next batch after this refill.
