# Day 18 — 2026-11-11

## Topic: Group Anagrams (Python)

**Problem:** Given a list of words, group together the ones that are
anagrams of each other — e.g. `["eat", "tea", "tan", "ate", "nat", "bat"]`
→ `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`.

## What I learned

- Anagrams share a canonical key: the word's letters sorted. `"eat"` and
  `"tea"` both sort to `"aet"`, so sorting turns "are these anagrams?"
  into a dictionary lookup.
- A `defaultdict(list)` keyed by that sorted tuple collects each group in
  one pass — no comparing every word against every other word (O(n²)).
- Sorting each word costs O(k log k) for a word of length k, so the whole
  thing is O(n · k log k); counting letters instead (26 counts as the key)
  would make it O(n · k), the standard follow-up optimisation.
- The order of groups and of words inside a group is not specified by the
  problem — tests should compare sorted groups, not exact list order.

## Code

See [`group_anagrams.py`](group_anagrams.py) in this folder.

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())
```

## Example

`group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])`
→ `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (group order may vary).
`group_anagrams([])` → `[]`.
`group_anagrams([""])` → `[[""]]`.

## Next

Debounce in JavaScript: a tiny higher-order function that makes a
rapid-fire handler (search input, window resize) run only once things
settle.
