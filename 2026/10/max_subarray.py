"""Day 3 — Maximum Subarray (LeetCode 53, Kadane's algorithm).

Given an integer array nums, find the contiguous subarray (containing at
least one number) with the largest sum, and return that sum.

Approach: Kadane's algorithm — walk the array once, keeping two values:
  * current_sum: the best sum of a subarray ending at this position.
  * best_sum:    the best sum seen anywhere so far.
At each number, decide: extend the previous subarray (current_sum + x) or
start fresh at x (just x). Whichever is larger becomes the new current_sum,
and best_sum tracks the maximum of those.

Why it works: any subarray ending before this position that drags the sum
down is worth dropping — a fresh start can only do better. This greedy
choice is safe because the best subarray ending here never depends on
anything except the best subarray ending at the previous position.

Time:  O(n)  — a single pass.
Space: O(1)  — only two running numbers, no extra array.
"""


def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any contiguous subarray of nums."""
    if not nums:
        raise ValueError("nums must contain at least one number")

    current_sum = best_sum = nums[0]
    for x in nums[1:]:
        # Extend the running subarray, or start a new one at x.
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


def max_subarray_with_bounds(nums: list[int]) -> tuple[int, int, int]:
    """Return (best_sum, start_index, end_index) of the best subarray."""
    if not nums:
        raise ValueError("nums must contain at least one number")

    current_sum = best_sum = nums[0]
    start = best_start = best_end = 0
    for i, x in enumerate(nums[1:], start=1):
        if x > current_sum + x:
            current_sum = x
            start = i
        else:
            current_sum += x
        if current_sum > best_sum:
            best_sum, best_start, best_end = current_sum, start, i
    return best_sum, best_start, best_end


def _run_tests() -> None:
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),   # classic example
        ([1], 1),                                # single element
        ([5, 4, -1, 7, 8], 23),                 # mostly positive
        ([-1, -2, -3], -1),                     # all negative: least bad wins
        ([0, 0, 0], 0),                         # all zeros
        ([-2, -1], -1),                         # two negatives
        ([3, -2, 5, -1], 6),                    # best spans the dip
    ]
    passed = 0
    for nums, expected in cases:
        got = max_subarray(nums)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: max_subarray({nums}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1

    # Bounds version agrees with the sum version, and slices check out.
    total, lo, hi = max_subarray_with_bounds([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert (total, lo, hi) == (6, 3, 6), (total, lo, hi)
    assert sum([-2, 1, -3, 4, -1, 2, 1, -5, 4][lo:hi + 1]) == total
    print(f"PASS: bounds version -> sum {total}, subarray [{lo}:{hi + 1}]")
    passed += 1

    print(f"\n{passed}/{len(cases) + 1} tests passed")
    assert passed == len(cases) + 1, "some tests failed"


if __name__ == "__main__":
    _run_tests()
