# Day 33 — Daily Temperatures (Python).
# A monotonic decreasing stack holds indices waiting for a warmer day;
# when a hotter temperature arrives, it answers every cooler day below it.
# Self-test (no network): python3 daily_temperatures.py


def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # indices of days still waiting for a warmer day
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    check("example [73,74,75,71,69,72,76,73]",
          daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
          [1, 1, 4, 2, 1, 1, 0, 0])
    # 2. Strictly rising: every day waits exactly one day.
    check("rising [30,40,50,60]",
          daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
    # 3. Strictly falling: no day ever gets warmer.
    check("falling [60,50,40,30]",
          daily_temperatures([60, 50, 40, 30]), [0, 0, 0, 0])
    # 4. Equal temperatures do not count as warmer.
    check("equal [70,70,71]",
          daily_temperatures([70, 70, 71]), [2, 1, 0])
    # 5. Single day.
    check("single [55]", daily_temperatures([55]), [0])
    # 6. Empty input.
    check("empty []", daily_temperatures([]), [])

    total = 6
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
