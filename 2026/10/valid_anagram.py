"""Day 2 — Valid Anagram (LeetCode 242).

Given two strings s and t, return True if t is an anagram of s
(same letters, same counts, any order) and False otherwise.

Approach: hash map counts — count the characters of s, then
decrement with t. If every count returns to zero, it's an anagram.

Time:  O(n)  — each string is scanned once.
Space: O(k)  — one entry per distinct character (k <= alphabet size).
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    return True


def _run_tests() -> None:
    cases = [
        (("anagram", "nagaram"), True),    # classic anagram
        (("rat", "car"), False),           # same length, different letters
        (("a", "ab"), False),              # different lengths
        (("", ""), True),                  # both empty
        (("aab", "abb"), False),           # same letters, different counts
        (("listen", "silent"), True),      # real-word anagram
        (("Triangle", "Integral"), False), # case-sensitive: not anagrams here
        (("hello123", "321olleh"), True),  # letters + digits
    ]
    passed = 0
    for (s, t), expected in cases:
        got = is_anagram(s, t)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: is_anagram({s!r}, {t!r}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
