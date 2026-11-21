# Day 25 — Merge Intervals (Python).
# Given intervals [start, end], merge every overlapping pair and
# return the disjoint intervals that cover the same ranges.
# Sort by start first: after that, overlaps can only run forward,
# so one pass is enough.
# Self-test (no network): python3 merge_intervals.py


def merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [[1,3],[2,6],[8,10],[15,18]]",
          merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
          [[1, 6], [8, 10], [15, 18]])

    # 2. Touching intervals merge (end == next start).
    check("touching [[1,4],[4,5]]",
          merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

    # 3. Unsorted input still merges.
    check("unsorted [[8,10],[1,3],[2,6]]",
          merge_intervals([[8, 10], [1, 3], [2, 6]]),
          [[1, 6], [8, 10]])

    # 4. One interval fully inside another.
    check("nested [[1,4],[2,3]]",
          merge_intervals([[1, 4], [2, 3]]), [[1, 4]])

    # 5. No overlaps: input comes back unchanged.
    check("disjoint [[1,2],[3,4]]",
          merge_intervals([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    # 6. Empty input.
    check("empty", merge_intervals([]), [])

    # 7. Single interval.
    check("single [[5,7]]", merge_intervals([[5, 7]]), [[5, 7]])

    total = 7
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
