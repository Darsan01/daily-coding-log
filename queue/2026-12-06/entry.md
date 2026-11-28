# Day 37 — 2026-12-06

## Topic: Word Break (Python)

**Problem:** Given a string and a dictionary of words, decide whether the string can be split into dictionary words — `"leetcode"`, `["leet", "code"]` → `True`; `"catsandog"` → `False`.

## What I learned

- This is a reachability question, not a matching one: `dp[i]` records whether the first `i` characters can be segmented, and each position only needs one earlier cut point `j` where `dp[j]` is True and `s[j:i]` is a word.
- The empty prefix is the base case that makes the loop work: `dp[0] = True` means "nothing to segment yet", so the first word can start at position 0.
- A greedy first match is a trap — `"catsandog"` starts with `"cat"` and `"cats"`, both real words, yet neither leads to a full split, which is why the DP checks every cut point instead of taking the first one.
- Turning the word list into a set matters: every `s[j:i]` lookup is O(1), so the cost is O(n²) time for the cut-point pairs and O(n) space for the table.
- This is the same DP shape as Day 30's Coin Change — build the answer for longer prefixes from shorter ones — applied to a string instead of an amount.

## Code

See [`word_break.py`](word_break.py) in this folder.

```python
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]
```

## Example

`"leetcode"`, `["leet", "code"]` → `True`. `"applepenapple"`, `["apple", "pen"]` → `True` (a word can be reused). `"catsandog"`, `["cats", "dog", "sand", "and", "cat"]` → `False`.

## Next

Day 38 topic to be chosen — the next batch after this refill.
