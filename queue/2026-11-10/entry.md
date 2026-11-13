# Day 17 — 2026-11-10

## Topic: Longest Substring Without Repeating Characters (Python)

**Problem:** Given a string, find the length of the longest substring with
no repeated character — e.g. `"abcabcbb"` → 3 (`"abc"`), `"pwwkew"` → 3
(`"wke"`).

## What I learned

- A sliding window with two pointers (`left`, `right`) keeps the current
  window repeat-free: `right` only ever moves forward, and `left` jumps
  past the previous occurrence of a repeated character.
- A dictionary mapping each character to its last seen index is what makes
  the jump O(1): when `s[right]` was seen at index `i >= left`, the new
  window must start at `i + 1` — anything earlier still contains the repeat.
- The `seen[ch] >= left` guard matters: a character seen before the window
  started is not a repeat inside the window, so `left` must never move
  backwards (the `"abba"` case catches this — the second `a` is fine
  because the first `a` is already outside the window).
- The whole scan is O(n) time and O(min(n, alphabet)) space — one pass,
  no nested loop, no rebuilding substrings.

## Code

See [`longest_substring.py`](longest_substring.py) in this folder.

```python
def length_of_longest_substring(s: str) -> int:
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

## Example

`length_of_longest_substring("abcabcbb")` → 3.
`length_of_longest_substring("bbbbb")` → 1.
`length_of_longest_substring("pwwkew")` → 3.
`length_of_longest_substring("dvdf")` → 3.
`length_of_longest_substring("")` → 0.

## Next

Group Anagrams (Python): same hash-map thinking, grouping words by their
sorted letters instead of tracking positions.
