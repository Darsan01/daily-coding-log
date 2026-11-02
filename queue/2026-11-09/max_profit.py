"""Day 16 — Best Time to Buy and Sell Stock (LeetCode 121).

Given daily stock prices, choose one day to buy and a later day to
sell to maximise profit, or return 0 if no profit is possible.

Approach: one pass. Track the lowest price seen so far; at each day,
profit if sold today is price - min_price, and the best of those is
the answer. No need to compare every buy/sell pair.

Time:  O(n). Space: O(1).
"""


def max_profit(prices: list[int]) -> int:
    """Return the maximum profit from one buy and one later sell, or 0."""
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


def _run_tests() -> None:
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([1], 0),
        ([3, 2, 6, 5, 0, 3], 4),
        ([1, 2], 1),
    ]
    passed = 0
    for prices, expected in cases:
        got = max_profit(prices)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: max_profit({prices}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
