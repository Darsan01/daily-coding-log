# Day 34 — 2026-12-03

## Topic: Number of Islands (Python)

**Problem:** Given a grid of `"1"` (land) and `"0"` (water), count the islands — groups of land connected horizontally or vertically. The textbook 4×5 grid with three separate groups → `3`.

## What I learned

- Counting islands is counting flood-fills: every unvisited `"1"` starts a new island, and the flood claims every land cell connected to it, so each island is counted exactly once, at its first cell.
- The `visited` set is what stops the flood from looping forever and from double-counting: a cell is marked the moment it is queued, not when it is popped, so it can never be queued twice.
- Only four directions count — up, down, left, right. Two land cells touching diagonally are separate islands, which is exactly what the `[["1","0"],["0","1"]]` test checks.
- Breadth-first search with a queue and depth-first search with a stack give the same count here; the queue version keeps the flood order easy to follow, and the grid itself is never modified — `visited` carries all the state.
- Cost is O(rows × cols) time, because every cell is visited at most once, and O(rows × cols) space in the worst case — the same "explore each thing once" shape as Day 17's sliding window, applied to a grid instead of a string.

## Code

See [`num_islands.py`](num_islands.py) in this folder.

```python
from collections import deque

def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in visited:
                continue
            islands += 1
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
    return islands
```

## Example

The 4×5 grid with three separate land groups → `3`. All water → `0`. A single `"1"` → `1`. Diagonal-only land → `2` islands.

## Next

Day 35 topic to be chosen — the next batch after this refill.
