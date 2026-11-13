#!/usr/bin/env python3
"""Day 17 — Longest Substring Without Repeating Characters (Python).

Sliding window + last-seen index map. O(n) time, O(min(n, alphabet)) space.
Self-test: python3 longest_substring.py
"""


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


if __name__ == "__main__":
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("abba", 2),
        ("au", 2),
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("tmmzuxt", 5),
    ]
    failed = 0
    for text, expected in cases:
        got = length_of_longest_substring(text)
        status = "pass" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: length_of_longest_substring({text!r}) = {got} (expected {expected})")
    print(f"{len(cases) - failed}/{len(cases)} tests passed")
    raise SystemExit(1 if failed else 0)
