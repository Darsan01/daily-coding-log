# Day 38 — 2026-12-07

## Topic: LRU Cache (Python)

**Problem:** A fixed-capacity cache with `get` and `put` in O(1): reading a key marks it recently used, and inserting past capacity evicts the least recently used key.

## What I learned

- Two jobs need doing at once — look a key up instantly, and know which key is oldest — so one structure does both: an `OrderedDict` is a hash map that also remembers insertion order.
- Every access moves the key to the end with `move_to_end`, so "most recently used" is always at the back and "least recently used" is always at the front — no timestamps, no scanning.
- Eviction is a single step: `popitem(last=False)` removes the front item, the least recently used, the moment the cache grows past capacity.
- A `get` is not free of side effects — it refreshes the key, which is exactly why the second test evicts key 2 instead of key 1 after key 1 was read.
- Updating an existing key must not count as growth: `put` on a present key refreshes its position and overwrites the value, and only then is the size checked, which the third test checks.
- Cost is O(1) time per operation and O(capacity) space — the same "order plus lookup" pairing as Day 18's Group Anagrams, where a dict carried the grouping and the key carried the identity.

## Code

See [`lru_cache.py`](lru_cache.py) in this folder.

```python
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
```

## Example

Capacity 2: `put(1, 1)`, `put(2, 2)`, `get(1)` → `1`, `put(3, 3)` evicts key 2, `get(2)` → `-1`.

## Next

Day 39 topic to be chosen — the next batch after this refill.
