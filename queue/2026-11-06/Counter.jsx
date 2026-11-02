// Day 13 — React: useState counter + useEffect data fetch (JSX).
//
// useState: value + setter; the setter re-renders with the new value.
// Use the functional form setCount(c => c + 1) to avoid stale state.
// useEffect with [] runs once on mount (the fetch shape). The cleanup
// function aborts the fetch if the component unmounts mid-request,
// so setState is never called on an unmounted component.
//
// To run: drop these components into any React starter (e.g. Vite)
// and render <App />. JSX is not executed by the test script below;
// the checks verify the patterns are present in this file.

import { useState, useEffect } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+</button>
      <button onClick={() => setCount((c) => c - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    async function load() {
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users', {
          signal: controller.signal,
        });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        setUsers(await response.json());
      } catch (err) {
        if (err.name !== 'AbortError') setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    load();
    return () => controller.abort(); // cleanup on unmount
  }, []);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>Error: {error}</p>;
  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}

export function App() {
  return (
    <div>
      <Counter />
      <UserList />
    </div>
  );
}
