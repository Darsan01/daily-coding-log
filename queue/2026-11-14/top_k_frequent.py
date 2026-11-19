# Day 21 — Top K Frequent Elements (Python).
# Return the k most frequent elements in O(n) time with bucket sort:
# count frequencies, bucket elements by frequency, then walk the
# buckets from the highest frequency down until k are collected.
# Self-test (no network): python3 top_k_frequent.py
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        # Order within the answer is not guaranteed, so compare sorted.
        ok = sorted(actual) == sorted(expected)
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [1,1,1,2,2,3] k=2",
          top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    # 2. k = 1 returns only the single most frequent element.
    check("k=1 returns the top element only",
          top_k_frequent([1, 1, 1, 2, 2, 3], 1), [1])

    # 3. All elements the same.
    check("all same [4,4,4,4] k=1",
          top_k_frequent([4, 4, 4, 4], 1), [4])

    # 4. k equals the number of distinct elements: return all of them.
    check("k covers all distinct elements",
          top_k_frequent([5, 5, 6, 7], 3), [5, 6, 7])

    # 5. All frequencies tied at 1: any k of them is correct.
    result = top_k_frequent([1, 2, 3], 2)
    ok = len(result) == 2 and set(result) <= {1, 2, 3}
    if not ok:
        failures += 1
    print(f"{'pass' if ok else 'FAIL'}: tied frequencies return any 2 = {result}")

    # 6. Negative numbers and a single-element array.
    check("negatives [-1,-1,2] k=1",
          top_k_frequent([-1, -1, 2], 1), [-1])
    check("single element [9] k=1",
          top_k_frequent([9], 1), [9])

    total = 7
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
