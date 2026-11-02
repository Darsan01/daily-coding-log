# Day 16 — 2026-11-09

## Topic: Best Time to Buy and Sell Stock (Python)
 (LeetCode 121)

**Problem:** Given daily stock prices, choose one day to buy and a later day to sell to maximise profit, or return 0 if no profit is possible. E.g. `[7, 1, 5, 3, 6, 4]` → `5` (buy at 1, sell at 6).

## What I learned

- One pass is enough: track the lowest price seen so far, and at each day compute profit if you sold today (price − min_price). The best of those is the answer — there is no need to compare every buy/sell pair.
- The greedy choice is safe here because the best sell day for a given buy day is simply the highest price after it, and the best buy day overall is the lowest price before that sell. Tracking the minimum as you go covers both at once.
- The all-falling case matters: prices `[7, 6, 4, 3, 1]` give profit `0`, not a negative number — you are allowed to not trade, so the answer is clamped at zero.
- Time: **O(n)**, space: **O(1)**. Compare the O(n²) brute force of every buy/sell pair — same answer, wildly different cost. This 'track the best so far' shape also solves maximum subarray (Day 3) and trailing-maximum problems.

## Code

See [`max_profit.py`](max_profit.py) in this folder, with tests.

```python
def max_profit(prices):
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best
```

## Example

`max_profit([7, 1, 5, 3, 6, 4])` → `5`, `max_profit([7, 6, 4, 3, 1])` → `0`, `max_profit([2, 4, 1])` → `2`.

## Next

Valid Anagram revisited? No — next: Two Sum II on a sorted array, the two-pointer sequel.
