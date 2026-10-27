# Day 7 — 2026-10-31

## Topic: Valid Parentheses — Stack (Python)
 (LeetCode 20)

**Problem:** Given a string `s` containing only `()[]{ }`, determine if the input is valid: open brackets must be closed by the same type, in the correct order. E.g. `"()[]{}"` → `True`; `"(]"` → `False`; `"([)]"` → `False`.

## What I learned

- A stack is the natural fit: the most recently opened bracket is the one that must close first — last in, first out. Every opening bracket gets pushed; every closing bracket must match the top of the stack.
- Three failure modes, all cheap to check: a closer with an empty stack, a closer that doesn't match the top, and a non-empty stack at the end (unclosed openers).
- A small dict mapping closers to openers (`{')': '(', ']': '[', '}': '{'}`) replaces a chain of ifs and makes the matching check one line.
- Time: **O(n)**. Space: **O(n)** in the worst case (all openers). This same stack idea shows up in expression evaluation, undo history, and parsing HTML/XML tags.

## Code

See [`valid_parentheses.py`](valid_parentheses.py) in this folder, with tests.

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
```

## Example

`is_valid("()[]{}")` → `True`, `is_valid("(]")` → `False`, `is_valid("([)]")` → `False`, `is_valid("")` → `True`.

## Next

FizzBuzz in JavaScript: the classic first JS problem — modulo, loops, and string building.
