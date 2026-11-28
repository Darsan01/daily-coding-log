# Day 30 — Coin Change (Python).
# Fewest coins to make an amount: dynamic programming over amounts.
# dp[x] is the fewest coins for x, built from dp[x - coin] + 1.
# Self-test (no network): python3 coin_change.py


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example: 5 + 5 + 1.
    check("example [1,2,5] amount 11", coin_change([1, 2, 5], 11), 3)
    # 2. Impossible amount.
    check("impossible [2] amount 3", coin_change([2], 3), -1)
    # 3. Zero amount needs zero coins.
    check("zero [1] amount 0", coin_change([1], 0), 0)
    # 4. Only 1s available.
    check("ones [1] amount 2", coin_change([1], 2), 2)
    # 5. Greedy would fail here: 3 + 3 beats 4 + 1 + 1.
    check("greedy trap [1,3,4] amount 6", coin_change([1, 3, 4], 6), 2)
    # 6. Mixed coins: four 2s plus a 5.
    check("mixed [2,5,10] amount 13", coin_change([2, 5, 10], 13), 5)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
