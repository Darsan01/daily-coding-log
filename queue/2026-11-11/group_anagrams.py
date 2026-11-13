#!/usr/bin/env python3
"""Day 18 — Group Anagrams (Python).

Group words by their sorted letters as a canonical key.
Self-test: python3 group_anagrams.py
"""
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def _normalised(groups):
    """Sort words inside each group and sort the groups, for comparison."""
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]],
        ),
        ([], []),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),
        (["listen", "silent", "enlist", "hello"], [["enlist", "listen", "silent"], ["hello"]]),
    ]
    failed = 0
    for words, expected in cases:
        got = _normalised(group_anagrams(words))
        status = "pass" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: group_anagrams({words}) = {got} (expected {expected})")
    print(f"{len(cases) - failed}/{len(cases)} tests passed")
    raise SystemExit(1 if failed else 0)
