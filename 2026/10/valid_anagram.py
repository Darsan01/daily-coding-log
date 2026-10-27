def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s.

    Key idea: two strings are anagrams when they contain exactly the same
    letters with the same frequencies, regardless of order. Count the
    letters of each string with a hash map and compare the counts.
    """
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


def is_anagram_sorted(s: str, t: str) -> bool:
    """Simpler alternative: sort both strings and compare.

    Easier to write, but slower — sorting costs O(n log n) time.
    """
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "bello", False),
        ("", "", True),
        ("a", "a", True),
        ("aab", "aba", True),
        ("aab", "abb", False),
        ("Dormitory", "dirty room", False),  # spaces/case not normalised
    ]
    for s, t, expected in cases:
        got = is_anagram(s, t)
        assert got == expected, f"is_anagram({s!r}, {t!r}) = {got}, expected {expected}"
        assert is_anagram_sorted(s, t) == expected
    print(f"All {len(cases)} test cases passed.")
