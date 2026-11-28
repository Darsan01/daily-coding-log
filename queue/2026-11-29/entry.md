# Day 30 — 2026-11-29

## Topic: Coin Change (Python)

**Problem:** Given coin denominations and an amount, return the fewest coins needed to make that amount — `[1, 2, 5]`, amount `11` → `3` (5 + 5 + 1). Return `-1` if the amount cannot be made.

## What I learned

- Greedy fails here, which is the point of the problem: with coins `[1, 3, 4]`, grabbing the biggest coin first gives 4 + 1 + 1 (three coins) for amount 6, while 3 + 3 needs only two — so the answer has to consider every coin at every amount, not just the biggest one.
- The DP table is one row, not a grid: `dp[x]` is the fewest coins for amount `x`, and it is built from `dp[x - coin] + 1` — one more coin on top of the best answer for the smaller amount that coin leaves behind.
- The sentinel value does double duty: `dp` starts at `amount + 1`, a count no real answer can reach (at most `amount` coins of value 1), so a cell still holding the sentinel at the end means "unreachable" and becomes the `-1` answer.
- The order of the loops matters for the story, not the answer: iterating coins outside and amounts inside still fills every `dp[x]` from smaller amounts, because each coin's pass only ever reads `dp[x - coin]`, which is already settled for that coin.
- This is Day 15's Climbing Stairs grown up: there the step sizes were fixed at 1 and 2 and the question was how many ways; here the step sizes are the coins and the question is the fewest steps — same "answer for x from answers for smaller x" shape, different question.

## Code

See [`coin_change.py`](coin_change.py) in this folder.

```python
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1
```

## Example

`[1, 2, 5]`, `11` → `3`. `[2]`, `3` → `-1`. `[1]`, `0` → `0`. `[1, 3, 4]`, `6` → `2` (3 + 3, not 4 + 1 + 1).

## Next

Day 31 topic to be chosen — the next batch after this refill.
