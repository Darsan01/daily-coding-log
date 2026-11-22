# Day 28 — 3Sum (Python).
# Return all unique triplets [a, b, c] with a + b + c == 0.
# Sort first, fix one number, then two pointers for the pair.
# Self-test (no network): python3 three_sum.py


def three_sum(nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example, duplicate -1 must not double the triplet.
    check("example [-1,0,1,2,-1,-4]",
          three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    # 2. All zeros give exactly one triplet.
    check("all zeros [0,0,0]", three_sum([0, 0, 0]), [[0, 0, 0]])
    # 3. No triplet sums to zero.
    check("no triplet [1,2,3]", three_sum([1, 2, 3]), [])
    # 4. Too few numbers.
    check("too few [0,1,1]", three_sum([0, 1, 1]), [])
    # 5. Empty input.
    check("empty []", three_sum([]), [])
    # 6. Extra duplicates collapse to one triplet each.
    check("duplicates [-2,0,0,2,2]",
          three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
