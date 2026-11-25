# Day 34 — Number of Islands (Python).
# Flood-fill each unvisited '1' and count the flood: one flood, one island.
# Self-test (no network): python3 num_islands.py
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


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example: one island.
    check("one island", num_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]), 1)
    # 2. Textbook example: three islands.
    check("three islands", num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]), 3)
    # 3. All water.
    check("all water", num_islands([
        ["0", "0"], ["0", "0"]]), 0)
    # 4. Single land cell.
    check("single land", num_islands([["1"]]), 1)
    # 5. Diagonal land does not connect (only 4 directions).
    check("diagonal only", num_islands([
        ["1", "0"], ["0", "1"]]), 2)
    # 6. Empty grid.
    check("empty []", num_islands([]), 0)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
