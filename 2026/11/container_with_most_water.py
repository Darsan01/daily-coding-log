# Day 23 — Container With Most Water (Python).
# Given heights of vertical lines, find two lines that together with
# the x-axis form a container holding the most water.
# Two pointers: start wide, move the shorter side inward.
# Self-test (no network): python3 container_with_most_water.py


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        area = width * min(height[left], height[right])
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    check("classic [1,8,6,2,5,4,8,3,7]", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check("two lines [1,1]", max_area([1, 1]), 1)
    check("tall ends [4,3,2,1,4]", max_area([4, 3, 2, 1, 4]), 16)
    check("rising [1,2,3,4,5]", max_area([1, 2, 3, 4, 5]), 6)
    check("falling [5,4,3,2,1]", max_area([5, 4, 3, 2, 1]), 6)
    check("single line [5]", max_area([5]), 0)
    check("empty []", max_area([]), 0)
    check("equal heights [3,3,3,3]", max_area([3, 3, 3, 3]), 9)

    total = 8
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
