"""Day 4 — Valid Palindrome (LeetCode 125, Two Pointers).

A phrase is a palindrome if, after converting all uppercase letters to
lowercase and removing all non-alphanumeric characters, it reads the
same forward and backward.

Approach: two pointers, one at each end, moving inward. Skip any
character that is not alphanumeric, compare the pair (lowercased), and
stop as soon as a pair disagrees.

Time:  O(n)  — each character is visited at most once.
Space: O(1)  — no cleaned copy of the string is built.
"""


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome ignoring case and non-alphanumerics."""
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


def _run_tests() -> None:
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("a", True),
        ("0P", False),
        ("Madam", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("12345", False),
    ]
    passed = 0
    for text, expected in cases:
        got = is_palindrome(text)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: is_palindrome({text!r}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
