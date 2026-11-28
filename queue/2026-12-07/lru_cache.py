# Day 38 — LRU Cache (Python).
# Least-recently-used cache in O(1) per operation: an OrderedDict keeps
# insertion order, and every access moves the key to the end, so the
# front is always the least recently used.
# Self-test (no network): python3 lru_cache.py
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def main():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        if not ok:
            failures += 1
        print(f"{'pass' if ok else 'FAIL'}: {name} = {actual} (expected {expected})")

    # 1. Textbook example.
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    check("example get(1)", c.get(1), 1)
    c.put(3, 3)  # evicts key 2
    check("example get(2) evicted", c.get(2), -1)
    c.put(4, 4)  # evicts key 1
    check("example get(1) evicted", c.get(1), -1)
    check("example get(3)", c.get(3), 3)
    check("example get(4)", c.get(4), 4)
    # 2. Reading a key refreshes it, so a different key is evicted.
    c2 = LRUCache(2)
    c2.put(1, 10)
    c2.put(2, 20)
    c2.get(1)
    c2.put(3, 30)  # evicts key 2, not key 1
    check("get refreshes get(1)", c2.get(1), 10)
    check("get refreshes get(2) evicted", c2.get(2), -1)
    # 3. Updating an existing key does not grow the cache.
    c3 = LRUCache(1)
    c3.put(1, 1)
    c3.put(1, 99)
    check("update keeps one entry", c3.get(1), 99)

    total = 9
    print(f"{total - failures}/{total} tests passed" if failures == 0
          else f"{failures} test(s) failed")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
