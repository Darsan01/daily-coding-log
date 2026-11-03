# Day 9 — 2026-11-02

## Topic: Array map / filter / reduce (JavaScript)


**Problem:** Given an array of numbers, use `map`, `filter`, and `reduce` — no manual loops — to: double every number, keep only the even ones, and sum the result. Then apply the same three methods to a small real example: total price of items in a cart.

## What I learned

- Three verbs cover most array work: `map` transforms every element (same length out), `filter` keeps a subset (shorter or equal), `reduce` folds everything into one value. Chaining them reads like the problem statement.
- Each method returns a **new** array (or value) — the original is untouched. That immutability is why these play well with React state, where mutating an array in place is a bug.
- Arrow functions make the callbacks short, but the callback's return value is the whole contract: forget `return` in a block-bodied arrow and `map` fills the array with `undefined`.
- The cart example shows why `reduce` takes an initial value: `reduce((sum, item) => sum + item.price * item.qty, 0)` — the `0` is the starting total, and without it an empty cart throws.

## Code

See [`array_methods.js`](array_methods.js) in this folder, with tests.

```javascript
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(n => n * 2);          // [2, 4, 6, 8, 10]
const evens = doubled.filter(n => n % 2 === 0); // all of them here
const total = evens.reduce((sum, n) => sum + n, 0); // 30
```

## Example

`total = [1,2,3,4,5].map(n => n * 2).filter(n => n % 2 === 0).reduce((s, n) => s + n, 0)` → `30`. Cart total example is in the code file.

## Next

SQL SELECT / JOIN: pull the right rows from two tables in one query.
