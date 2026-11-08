# Day 13 — 2026-11-06

## Topic: React — useState counter + useEffect data fetch (JSX)


**Problem:** Build a counter component (increment, decrement, reset) with useState, then a second component that fetches a user list with useEffect, shows a loading state, and cleans up properly if it unmounts mid-fetch.

## What I learned

- useState gives you a value and a setter; calling the setter re-renders the component with the new value. State updates are async — `setCount(count + 1)` twice in a row uses the same stale `count`, while the functional form `setCount(c => c + 1)` always uses the latest value.
- useEffect runs after render. The empty dependency array `[]` means 'run once on mount' — the right shape for a data fetch. Leaving the array out runs the effect after every render (and re-fetches forever); listing a value in it re-runs the effect only when that value changes.
- Cleanup matters: if the component unmounts while a fetch is in flight, setting state afterwards warns (and in older React, leaks). An AbortController in the cleanup function cancels the fetch — the code file shows exactly that pattern.
- State belongs in the component that needs it. Lifting the counter state into a parent is what lets two components share it; keeping it local is what keeps components reusable.

## Code

See [`Counter.jsx`](Counter.jsx) in this folder, with tests.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>+</button>
      <button onClick={() => setCount(c => c - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

## Example

The file also includes a `UserList` component with loading / error / data states and an AbortController cleanup, plus notes on how to run it (any React starter, e.g. Vite). JSX isn't executed here, so the tests check the file's structure (hooks used, cleanup present) instead of running it.

## Next

Merge Two Sorted Lists: walk both lists at once, always taking the smaller head.
