# Day 29 — 2026-11-28

## Topic: Longest Common Prefix (Python)

**Problem:** Given a list of strings, return the longest string that is a prefix of every one of them — `["flower", "flow", "flight"]` → `"fl"`. If there is no common prefix, return `""`.

## What I learned

- The shrink-until-it-fits idea is the whole algorithm: start with the first string as the candidate prefix, then for each later string keep chopping the last character off until that string starts with what remains. The candidate can only get shorter, never longer.
- `str.startswith(prefix)` does the checking work — there is no need to compare character by character by hand, and the loop condition reads exactly like the problem statement.
- The empty string is the natural failure case, not a special one: once the prefix shrinks to `""`, every string starts with it, so returning `""` there is both correct and the only sensible answer when the strings share nothing.
- An empty input list needs its own guard up front, because there is no first string to start from — without it, `strs[0]` raises an `IndexError` before any real work happens.
- Cost is O(S) time, where S is the total number of characters across all strings, and O(1) extra space beyond the prefix itself — the same "first string as the running answer" shape as Day 16's best-price scan, applied to strings instead of numbers.

## Code

See [`longest_common_prefix.py`](longest_common_prefix.py) in this folder.

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

## Example

`["flower", "flow", "flight"]` → `"fl"`. `["dog", "racecar", "car"]` → `""`. `["interspecies", "interstellar", "interstate"]` → `"inters"`. A single `["single"]` → `"single"`, and `[]` → `""`.

## Next

Day 30 topic to be chosen — the next batch after this refill.
