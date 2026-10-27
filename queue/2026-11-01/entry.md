# Day 8 — 2026-11-01

## Topic: FizzBuzz (JavaScript)


**Problem:** Print the numbers from 1 to 100, but for multiples of 3 print `"Fizz"` instead, for multiples of 5 print `"Buzz"`, and for multiples of both print `"FizzBuzz"`.

## What I learned

- Order of the checks matters: test the 15-case first (or build the string from parts). Checking 3 first swallows the 15s and the "FizzBuzz" case never fires — the most common FizzBuzz bug.
- Building the output string by appending ("Fizz" if divisible by 3, "Buzz" if divisible by 5, else the number) is cleaner than a four-way if/else, and it scales to extra rules like "Bang" for 7.
- Modulo is the workhorse here: `n % 3 === 0` is just asking "does 3 divide n evenly?". Same operator, different problem: even/odd, wrapping an index, cycling through a list.
- The function version in the code file returns an array instead of printing, so it can be tested — `fizzbuzz(15)` ends with `[..., "Fizz", 14, "FizzBuzz"]`.

## Code

See [`fizzbuzz.js`](fizzbuzz.js) in this folder, with tests.

```javascript
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
```

## Example

`fizzbuzz(15)` → `[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]`.

## Next

Array map / filter / reduce in JavaScript: transform, keep, and combine — the core of everyday JS.
