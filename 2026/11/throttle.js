// Day 20 — Throttle in JavaScript.
// Returns a function that runs `fn` at most once per `limit` ms:
// the first call runs immediately, later calls inside the window are
// collapsed into one trailing call with the latest arguments.
// Self-test (no network, timers only): node throttle.js
"use strict";

function throttle(fn, limit) {
  let lastRun = 0;
  let timer = null;
  let lastArgs = null;
  let lastThis = null;
  return function (...args) {
    const now = Date.now();
    const remaining = limit - (now - lastRun);
    if (remaining <= 0) {
      if (timer) {
        clearTimeout(timer);
        timer = null;
      }
      lastRun = now;
      fn.apply(this, args);
    } else {
      // Inside the window: remember the latest call and run it once,
      // when the window ends, instead of running every call.
      lastArgs = args;
      lastThis = this;
      if (!timer) {
        timer = setTimeout(() => {
          timer = null;
          lastRun = Date.now();
          fn.apply(lastThis, lastArgs);
        }, remaining);
      }
    }
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

  // 1. Five rapid calls -> leading run + one trailing run with the last arg.
  let calls = [];
  const throttled = throttle((text) => calls.push(text), 50);
  throttled("a");
  throttled("ab");
  throttled("abc");
  throttled("abcd");
  throttled("abcde");
  check("first call runs immediately", calls, ["a"]);
  await sleep(100);
  check("rapid calls collapse to leading + trailing with last arg", calls, ["a", "abcde"]);

  // 2. Calls spaced wider than the limit -> one run each, no trailing.
  calls = [];
  const slow = throttle((text) => calls.push(text), 20);
  slow("first");
  await sleep(40);
  slow("second");
  await sleep(40);
  check("spaced calls run each time", calls, ["first", "second"]);

  // 3. `this` and arguments are preserved on the trailing call.
  const obj = {
    prefix: "scroll:",
    seen: [],
    onScroll(pos) {
      this.seen.push(this.prefix + pos);
    },
  };
  obj.onScrollThrottled = throttle(obj.onScroll, 40);
  obj.onScrollThrottled(10);
  obj.onScrollThrottled(20);
  await sleep(80);
  check("this and latest args preserved", obj.seen, ["scroll:10", "scroll:20"]);

  // 4. Nothing runs after the window settles — no extra trailing call.
  calls = [];
  const quiet = throttle((text) => calls.push(text), 30);
  quiet("only");
  await sleep(80);
  check("single call runs once, no phantom trailing run", calls, ["only"]);

  // 5. A call after the window has fully passed runs immediately again.
  calls = [];
  const again = throttle((text) => calls.push(text), 30);
  again("one");
  await sleep(60);
  again("two");
  check("call after window runs immediately", calls, ["one", "two"]);
  await sleep(60);
  check("no trailing run after a leading call", calls, ["one", "two"]);

  const total = 6;
  console.log(failures === 0 ? `${total}/${total} tests passed` : `${failures} test(s) failed`);
  process.exit(failures === 0 ? 0 : 1);
}

main();
