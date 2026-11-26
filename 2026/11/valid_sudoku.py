# Day 27 — Valid Sudoku (Python).
# Only the filled cells need to be valid: no digit repeats in any
# row, column, or 3x3 box. Empty cells are "." and are skipped.
# Self-test (no network): python3 valid_sudoku.py


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


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    # 1. Classic valid partial board.
    check("valid partial board", is_valid_sudoku([row[:] for row in valid]), True)
    # 2. Duplicate 3 in the top-left 3x3 box only (row 2, col 0 was ".";
    # row 2 and column 0 contain no 3, the box already has one at [0][1]).
    box_dup = [row[:] for row in valid]
    box_dup[2][0] = "3"
    check("duplicate in box", is_valid_sudoku(box_dup), False)
    # 3. Duplicate 5 in column 0 (row 2, col 0 was ".").
    col_dup = [row[:] for row in valid]
    col_dup[2][0] = "5"
    check("duplicate in column", is_valid_sudoku(col_dup), False)
    # 4. Duplicate 3 in row 0 (row 0, col 2 was ".").
    row_dup = [row[:] for row in valid]
    row_dup[0][2] = "3"
    check("duplicate in row", is_valid_sudoku(row_dup), False)
    # 5. All-empty board is valid.
    check("empty board", is_valid_sudoku([["."] * 9 for _ in range(9)]), True)
    # 6. Single filled cell is valid.
    single = [["."] * 9 for _ in range(9)]
    single[4][4] = "7"
    check("single cell", is_valid_sudoku(single), True)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
