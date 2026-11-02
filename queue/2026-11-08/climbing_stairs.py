"""Day 15 — Climbing Stairs (LeetCode 70, Dynamic Programming).

You are climbing a staircase with n steps. Each time you can climb 1
or 2 steps. In how many distinct ways can you climb to the top?

Approach: the last step is a 1-step or a 2-step, so
ways(n) = ways(n-1) + ways(n-2) — Fibonacci in disguise. Naive
recursion recomputes subproblems exponentially; rolling just the
previous two values forward gives O(n) time and O(1) space.
"""


def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb n steps (1 or 2 at a time)."""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


def _run_tests() -> None:
    cases = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (10, 89), (45, 1836311903)]
    passed = 0
    for n, expected in cases:
        got = climb_stairs(n)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: climb_stairs({n}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
