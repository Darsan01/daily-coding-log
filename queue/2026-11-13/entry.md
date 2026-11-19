# Day 20 — 2026-11-13

## Topic: Throttle in JavaScript

**Problem:** A scroll handler fires dozens of times a second, but the
work it does (e.g. updating a sticky header) only needs to happen at
most once every 100 ms — and it must still run while the user keeps
scrolling, not only after they stop.

## What I learned

- Throttle is the companion to debounce (Day 19): debounce waits for a
  pause, throttle guarantees a call at most every N ms while activity
  continues — the right choice for scroll, resize and mousemove, the
  wrong one for search-as-you-type.
- The leading call runs immediately, so the UI responds at once; calls
  inside the window are not dropped silently but collapsed into a
  single trailing call carrying the *latest* arguments, so the final
  scroll position is never lost.
- `lastRun` (a timestamp) decides whether a call is leading or inside
  the window; a single `timer` schedules the trailing call, and it is
  only created once per window — later calls inside the same window
  just overwrite the stored arguments.
- `fn.apply(this, args)` matters here too: without it the throttled
  handler loses both its arguments (the latest scroll position) and
  its `this`, so it would act on stale input.
- Clearing a pending trailing timer when a leading call runs keeps the
  two paths from double-firing on the same window boundary.

## Code

See [`throttle.js`](throttle.js) in this folder.

```js
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
      lastArgs = args; // latest call wins the trailing slot
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
const onScroll = throttle((pos) => updateHeader(pos), 100);
```

## Example

Call the throttled function 5 times in a row (limit 50 ms) → it runs
twice: once immediately with the first argument, once at the end of
the window with the last argument. Call it, wait longer than the
limit, call it again → it runs immediately each time, with no
trailing call.

## Next

Day 21 topic to be chosen — the next batch after this refill.
