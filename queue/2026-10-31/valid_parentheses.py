"""Day 7 — Valid Parentheses (LeetCode 20, Stack).

Given a string s containing only the characters ()[]{} , determine if
the input is valid: open brackets must be closed by the same type of
bracket, and in the correct order.

Approach: a stack. Push every opener; on a closer, the top of the stack
must be its matching opener. At the end the stack must be empty.

Time:  O(n). Space: O(n) in the worst case (all openers).
"""


def is_valid(s: str) -> bool:
    """Return True if s is a correctly nested bracket string."""
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack


def _run_tests() -> None:
    cases = [
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
        ("(()", False),
        ("[({})]", True),
    ]
    passed = 0
    for text, expected in cases:
        got = is_valid(text)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: is_valid({text!r}) -> {got} (expected {expected})")
        if got == expected:
            passed += 1
    print(f"\n{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "some tests failed"


if __name__ == "__main__":
    _run_tests()
