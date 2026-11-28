# Day 36 — Min Stack (Python).
# A stack that returns the current minimum in O(1): each entry stores
# its value alongside the minimum of everything below it.
# Self-test (no network): python3 min_stack.py


class MinStack:
    def __init__(self):
        self.stack = []  # each item: (value, min-so-far)

    def push(self, val):
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    check("example get_min after -2,0,-3", s.get_min(), -3)
    s.pop()
    check("example top after pop", s.top(), 0)
    check("example get_min after pop", s.get_min(), -2)
    # 2. Minimum updates when the smallest value is popped.
    s2 = MinStack()
    s2.push(5)
    s2.push(1)
    s2.push(4)
    check("min is 1", s2.get_min(), 1)
    s2.pop()
    check("min still 1 after popping 4", s2.get_min(), 1)
    s2.pop()
    check("min back to 5 after popping 1", s2.get_min(), 5)
    # 3. Duplicate minimums survive a pop.
    s3 = MinStack()
    s3.push(2)
    s3.push(2)
    s3.pop()
    check("duplicate min survives pop", s3.get_min(), 2)

    total = 8
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
