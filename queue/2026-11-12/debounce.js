// Day 19 — Debounce in JavaScript.
// Returns a function that only runs `fn` once calls stop for `wait` ms.
// Self-test (no network, timers only): node debounce.js
"use strict";

function debounce(fn, wait) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), wait);
  };
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function main() {
  let failures = 0;
  const check = (name, actual, expected) => {
    const ok = JSON.stringify(actual) === JSON.stringify(expected);
    if (!ok) failures += 1;
    console.log(`${ok ? "pass" : "FAIL"}: ${name} = ${JSON.stringify(actual)} (expected ${JSON.stringify(expected)})`);
  };

  // 1. Five rapid calls -> exactly one run, with the last argument.
  let calls = [];
  const debounced = debounce((text) => calls.push(text), 30);
  debounced("a");
  debounced("ab");
  debounced("abc");
  debounced("abcd");
  debounced("abcde");
  await sleep(60);
  check("rapid calls run once with last arg", calls, ["abcde"]);

  // 2. Calls separated by more than the wait -> one run each.
  calls = [];
  const slow = debounce((text) => calls.push(text), 20);
  slow("first");
  await sleep(40);
  slow("second");
  await sleep(40);
  check("spaced calls run each time", calls, ["first", "second"]);

  // 3. `this` and arguments are preserved.
  const obj = {
    prefix: "hit:",
    seen: [],
    search(text) {
      this.seen.push(this.prefix + text);
    },
  };
  obj.searchDebounced = debounce(obj.search, 20);
  obj.searchDebounced("x");
  await sleep(40);
  check("this and args preserved", obj.seen, ["hit:x"]);

  // 4. Nothing runs before the wait elapses.
  calls = [];
  const late = debounce((text) => calls.push(text), 50);
  late("too soon?");
  await sleep(20);
  check("no run before wait elapses", calls, []);
  await sleep(50);
  check("runs after wait elapses", calls, ["too soon?"]);

  const total = 5;
  console.log(failures === 0 ? `${total}/${total} tests passed` : `${failures} test(s) failed`);
  process.exit(failures === 0 ? 0 : 1);
}

main();
