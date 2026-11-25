# Day 29 — Longest Common Prefix (Python).
# Shrink the first string until every other string starts with it.
# Self-test (no network): python3 longest_common_prefix.py


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


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual!r} (expected {expected!r})")

    # 1. Textbook example.
    check('example ["flower","flow","flight"]',
          longest_common_prefix(["flower", "flow", "flight"]), "fl")
    # 2. No common prefix at all.
    check('no prefix ["dog","racecar","car"]',
          longest_common_prefix(["dog", "racecar", "car"]), "")
    # 3. Longer shared stem.
    check('long stem ["interspecies","interstellar","interstate"]',
          longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")
    # 4. A single string is its own prefix.
    check('single ["single"]', longest_common_prefix(["single"]), "single")
    # 5. Empty input has no prefix.
    check("empty []", longest_common_prefix([]), "")
    # 6. An empty string in the list kills the prefix.
    check('empty member ["","abc"]', longest_common_prefix(["", "abc"]), "")

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
