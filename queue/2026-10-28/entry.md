# Day 4 — 2026-10-28

## Topic: Valid Palindrome — Two Pointers (Python)
 (LeetCode 125)

**Problem:** Given a string `s`, return `True` if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters. E.g. `"A man, a plan, a canal: Panama"` → `True`; `"race a car"` → `False`.

## What I learned

- Two pointers, one at each end, moving inward — the classic pattern for anything symmetric. No extra string needed: compare `s[left]` and `s[right]`, skip anything that isn't alphanumeric, stop when the pointers cross.
- Doing it in place is **O(1)** extra space. The tempting shortcut — build a cleaned string and compare it to its reverse — is simpler to read but costs O(n) space.
- The fiddly part is the pointer movement: after a skip, re-check the loop condition before comparing, or the pointers can cross and compare the wrong pair. The `while left < right` guard on both inner loops handles it.
- Time: **O(n)** — each character is visited at most once. Space: **O(1)**.

## Code

See [`valid_palindrome.py`](valid_palindrome.py) in this folder, with tests.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

## Example

`is_palindrome("A man, a plan, a canal: Panama")` → `True`, `is_palindrome("race a car")` → `False`, `is_palindrome("")` → `True`.

## Next

Binary Search: halve the search space every step — O(log n).
