# Day 27 — 2026-11-26

## Topic: Valid Sudoku (Python)

**Problem:** Given a 9×9 Sudoku board filled with digits `1`–`9` and empty cells marked `.`, check whether the filled cells follow the rules — no digit repeats in any row, any column, or any of the nine 3×3 boxes. Only the filled cells need to be valid; the board does not have to be solvable.

## What I learned

- One pass with three sets of sets is enough: a set per row, a set per column, and a set per 3×3 box. A digit seen twice in any of them fails the board at once — there is no need to check rows, columns and boxes in separate passes.
- The box index is the neat part: `box = (row // 3) * 3 + (col // 3)`. Integer division by 3 groups rows and columns into threes, so every cell maps to exactly one of the nine boxes.
- Empty cells (`.`) are skipped, not treated as a value — putting them in the sets would make two empty cells in a row look like a repeat.
- The check is O(1) in practice: the board is always 9×9, so the work is bounded at 81 cells. The same set-lookup idea scales, though — it is the hash-set membership trick from Day 2's Valid Anagram and Day 18's Group Anagrams, applied to three dimensions at once.
- This is a validation problem, not a solving problem: it never fills a cell in, so there is no backtracking. That is why it stays simple while a full Sudoku solver is much harder.

## Code

See [`valid_sudoku.py`](valid_sudoku.py) in this folder.

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)
    return True
```

## Example

The classic valid partial board (with `.` for empty cells) → `True`. The same board with a second `3` in the top-left 3×3 box → `False`. A board with two `5`s in one column → `False`, even if every row is fine. An all-empty board → `True`.

## Next

Day 28 topic to be chosen — the next batch after this refill.
