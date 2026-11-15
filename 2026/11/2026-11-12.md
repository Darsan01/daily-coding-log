# Day 19 — 2026-11-12

## Topic: Debounce in JavaScript

**Problem:** A search box fires `oninput` on every keystroke, but the
lookup should only run once the user stops typing — e.g. 5 keystrokes in
200 ms should trigger exactly 1 search, with the latest text.

## What I learned

- Debounce is a higher-order function: it takes a function and a wait time
  and returns a new function that resets a timer on every call and only
  runs the original once the timer survives the full wait.
- `clearTimeout` + `setTimeout` is the whole mechanism — there is no
  library magic, and the timer id is closed over so each debounced
  function keeps its own independent timer.
- `fn.apply(this, args)` matters: without it the debounced function loses
  both its arguments (the latest keystroke's text) and its `this`, so the
  search would run with stale or missing input.
- Debounce is not throttle: throttle guarantees a call at most every N ms
  while activity continues; debounce waits for a pause, so a user who
  never stops typing never triggers it — the right choice for search, the
  wrong one for scroll position.

## Code

See [`debounce.js`](debounce.js) in this folder.

```js
function debounce(fn, wait) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), wait);
  };
}
const search = debounce((text) => lookup(text), 300);
```

## Example

Call the debounced function 5 times in 200 ms (wait 300 ms) → the
underlying function runs once, with the 5th call's argument.
Call it, wait 400 ms, call it again → it runs twice, once per pause.

## Next

Day 20 topic to be chosen — the next batch after this refill.
