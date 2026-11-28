# Day 37 — Word Break (Python).
# Can the string be split into dictionary words? A boolean DP table:
# dp[i] is True when the first i characters can be segmented.
# Self-test (no network): python3 word_break.py


def word_break(s, word_dict):
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example leetcode [leet,code]", word_break("leetcode", ["leet", "code"]), True)
    # 2. A word reused across the split.
    check("applepenapple [apple,pen]", word_break("applepenapple", ["apple", "pen"]), True)
    # 3. A tempting prefix that leads nowhere.
    check("catsandog [cats,dog,sand,and,cat]",
          word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
    # 4. Empty string needs no words.
    check("empty string", word_break("", ["a"]), True)
    # 5. Single letter, single word.
    check("single a [a]", word_break("a", ["a"]), True)
    # 6. Overlapping words, longest split wins.
    check("aaaaaaa [aaaa,aaa]", word_break("aaaaaaa", ["aaaa", "aaa"]), True)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
