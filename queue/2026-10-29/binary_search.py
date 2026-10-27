"""Day 5 — Binary Search (LeetCode 704).

Given a sorted array nums and a target, return the index of target,
or -1 if it is not present.

Approach: keep a window [left, right] that is guaranteed to contain
the answer if it exists. Look at the middle; if it is too small, the
answer must be to the right (left = mid + 1); if too big, to the left
(right = mid - 1). Each step halves the window.

Time:  O(log n) — the window halves every step.
Space: O(1).
"""


def binary_search(nums: list[int], target: int) -> int:
    """Return the index of target in sorted nums, or -1."""
    left, right = 0, len(nums) - 1
    while left <= right:
        # left + (right - left) // 2 avoids overflow in fixed-width ints.
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(nums: list[int], target: int) -> int:
    """Return the index of the first element >= target (insertion point)."""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def _run_tests() -> None:
    cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([], 1, -1),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        (list(range(0, 1_000_000, 2)), 999_998, 499_999),
    ]
    passed = 0
    for nums, target, expected in cases:
        got = binary_search(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: binary_search(..., {target}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    assert lower_bound([1, 3, 5, 7], 4) == 2
    assert lower_bound([1, 3, 5, 7], 7) == 3
    assert lower_bound([1, 3, 5, 7], 9) == 4
    print("PASS: lower_bound checks")
    passed += 1
    print(f"\n{passed}/{len(cases) + 1} tests passed")
    assert passed == len(cases) + 1, "some tests failed"


if __name__ == "__main__":
    _run_tests()
