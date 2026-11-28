# Day 32 — Kth Largest Element in an Array (Python).
# A min-heap of size k keeps only the k biggest values seen so far;
# its smallest element is the kth largest overall.
# Self-test (no network): python3 kth_largest.py
import heapq


def kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [3,2,1,5,6,4] k=2", kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
    # 2. Duplicates count separately.
    check("duplicates [3,2,3,1,2,4,5,5,6] k=4",
          kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
    # 3. k = 1 is the maximum.
    check("k=1 [7,2,9]", kth_largest([7, 2, 9], 1), 9)
    # 4. k = len(nums) is the minimum.
    check("k=len [7,2,9] k=3", kth_largest([7, 2, 9], 3), 2)
    # 5. Single element.
    check("single [42] k=1", kth_largest([42], 1), 42)
    # 6. Negative numbers.
    check("negatives [-1,-5,-3] k=2", kth_largest([-1, -5, -3], 2), -3)

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
