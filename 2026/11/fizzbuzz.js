// Day 8 — FizzBuzz (JavaScript).
//
// Print the numbers 1..n, but for multiples of 3 print "Fizz", for
// multiples of 5 print "Buzz", and for multiples of both "FizzBuzz".
// Building the string from parts (instead of a four-way if/else) means
// the 15-case can never be swallowed by the 3-case, and extra rules
// (e.g. "Bang" for 7) slot in with one line each.

function fizzbuzz(n) {
  const out = [];
  for (let i = 1; i <= n; i++) {
    let s = "";
    if (i % 3 === 0) s += "Fizz";
    if (i % 5 === 0) s += "Buzz";
    out.push(s || i);
  }
  return out;
}

function runTests() {
  const assert = require("node:assert");
  const cases = [
    [1, [1]],
    [3, [1, 2, "Fizz"]],
    [5, [1, 2, "Fizz", 4, "Buzz"]],
    [15, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]],
  ];
  let passed = 0;
  for (const [n, expected] of cases) {
    const got = fizzbuzz(n);
    assert.deepStrictEqual(got, expected);
    console.log(`PASS: fizzbuzz(${n}) -> [${got.join(", ")}]`);
    passed++;
  }
  const hundred = fizzbuzz(100);
  assert.strictEqual(hundred.length, 100);
  assert.strictEqual(hundred[99], "Buzz"); // 100 is a multiple of 5
  assert.strictEqual(hundred[29], "FizzBuzz"); // 30
  console.log("PASS: fizzbuzz(100) length and spot checks");
  passed++;
  console.log(`\n${passed}/${cases.length + 1} tests passed`);
}

if (require.main === module) {
  runTests();
  console.log(fizzbuzz(15).join(", "));
}

module.exports = { fizzbuzz };
