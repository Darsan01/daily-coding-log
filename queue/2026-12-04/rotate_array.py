# Day 35 — Rotate Array (Python).
# Rotate right by k in place with three reversals: reverse all,
# reverse the first k, reverse the rest.
# Self-test (no network): python3 rotate_array.py


def rotate(nums, k):
    n = len(nums)
    if n <= 1:
        return nums
    k %= n
    if k == 0:
        return nums
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [1,2,3,4,5,6,7] k=3", rotate([1, 2, 3, 4, 5, 6, 7], 3),
          [5, 6, 7, 1, 2, 3, 4])
    # 2. k larger than n wraps around.
    check("k>n [1,2,3] k=4", rotate([1, 2, 3], 4), [3, 1, 2])
    # 3. k = 0 changes nothing.
    check("k=0 [1,2,3]", rotate([1, 2, 3], 0), [1, 2, 3])
    # 4. k = n is a full turn.
    check("k=n [1,2,3] k=3", rotate([1, 2, 3], 3), [1, 2, 3])
    # 5. Single element.
    check("single [9] k=5", rotate([9], 5), [9])
    # 6. Negative numbers.
    check("negatives [-1,-100,3,99] k=2", rotate([-1, -100, 3, 99], 2),
          [3, 99, -1, -100])

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
