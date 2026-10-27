// Day 9 — Array map / filter / reduce (JavaScript).
//
// Three verbs cover most array work:
//   map    — transform every element (same length out)
//   filter — keep a subset
//   reduce — fold everything into one value
// Each returns a NEW array/value; the original is untouched, which is
// why they play well with React state (no in-place mutation).

const nums = [1, 2, 3, 4, 5];

const doubled = nums.map((n) => n * 2); // [2, 4, 6, 8, 10]
const evens = doubled.filter((n) => n % 2 === 0);
const total = evens.reduce((sum, n) => sum + n, 0); // 30

// Chained, as it would be written in real code:
const chainedTotal = nums
  .map((n) => n * 2)
  .filter((n) => n % 2 === 0)
  .reduce((sum, n) => sum + n, 0);

// Real example: total price of a shopping cart.
const cart = [
  { name: "Notebook", price: 4.5, qty: 2 },
  { name: "Pen", price: 1.2, qty: 5 },
  { name: "Backpack", price: 29.99, qty: 1 },
];
const cartTotal = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
const expensiveItems = cart.filter((item) => item.price > 5).map((item) => item.name);

function runTests() {
  const assert = require("node:assert");
  assert.deepStrictEqual(doubled, [2, 4, 6, 8, 10]);
  console.log("PASS: map doubles every number");
  assert.deepStrictEqual(evens, [2, 4, 6, 8, 10]);
  console.log("PASS: filter keeps the evens");
  assert.strictEqual(total, 30);
  assert.strictEqual(chainedTotal, 30);
  console.log("PASS: reduce sums to 30 (chained version agrees)");
  assert.deepStrictEqual(nums, [1, 2, 3, 4, 5]);
  console.log("PASS: original array untouched");
  assert.strictEqual(cartTotal.toFixed(2), "44.99");
  console.log(`PASS: cart total is £${cartTotal.toFixed(2)}`);
  assert.deepStrictEqual(expensiveItems, ["Backpack"]);
  console.log("PASS: expensive items are [Backpack]");
  assert.strictEqual([].reduce((s, n) => s + n, 0), 0);
  console.log("PASS: reduce with an initial value handles an empty array");
  console.log("\n7/7 tests passed");
}

if (require.main === module) {
  runTests();
  console.log({ doubled, evens, total, cartTotal: cartTotal.toFixed(2) });
}

module.exports = { doubled, evens, total, chainedTotal, cartTotal };
