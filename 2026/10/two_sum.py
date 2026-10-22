"""Day 1 — Two Sum (Python)

Given a list of numbers and a target, return the indices of the two
numbers that add up to the target.

Two approaches:
1. Brute force  — check every pair.        O(n^2) time, O(1) space.
2. Hash map     — one pass, store seen     O(n) time,   O(n) space.
   values in a dict and look up the
   complement (target - x) for each x.
"""


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
    for nums, target, expected in cases:
        assert two_sum(nums, target) == expected, (nums, target)
        assert two_sum_brute_force(nums, target) == expected, (nums, target)
    print("All Two Sum tests passed.")
