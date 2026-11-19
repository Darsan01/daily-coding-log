# Day 22 — Product of Array Except Self (Python).
# Return an array where each element is the product of all the other
# elements, in O(n) time and O(1) extra space (excluding the output):
# one left-to-right pass for prefix products, one right-to-left pass
# folding in suffix products. No division, so zeroes are handled.
# Self-test (no network): python3 product_except_self.py


def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [1,2,3,4]",
          product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    # 2. With a negative number.
    check("negatives [-1,1,0,-3,3]",
          product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    # 3. One zero: only its position is non-zero.
    check("one zero [1,2,0,4]",
          product_except_self([1, 2, 0, 4]), [0, 0, 8, 0])

    # 4. Two zeroes: every product is zero.
    check("two zeroes [1,0,3,0]",
          product_except_self([1, 0, 3, 0]), [0, 0, 0, 0])

    # 5. Two elements.
    check("two elements [2,3]",
          product_except_self([2, 3]), [3, 2])

    # 6. Single element: product of nothing is 1.
    check("single element [5]",
          product_except_self([5]), [1])

    # 7. All ones.
    check("all ones [1,1,1,1]",
          product_except_self([1, 1, 1, 1]), [1, 1, 1, 1])

    total = 7
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
