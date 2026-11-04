# Day 10 — 2026-11-03

## Topic: Fetch API — fetch and render JSON (JavaScript)


**Problem:** Fetch a list of users from a JSON API and render their names and emails — handling loading, success, and error states, without crashing if the network fails.

## What I learned

- fetch() returns a Promise that resolves to a Response, not to the data itself — you still have to call `response.json()`, which is itself async. Forgetting that second await is the classic first bug.
- Always check `response.ok` before parsing: fetch only rejects on network failure, not on a 404 or 500. A 404 still resolves, so an unchecked `.json()` can throw on an error page.
- Wrap the call in try/catch and track three states — loading, data, error — instead of one. Rendering 'Loading…' while waiting and a clear error message on failure is what makes a fetch feel finished rather than broken.
- async/await reads top-to-bottom like synchronous code, which is why it replaced nested `.then()` chains for this kind of work. The code file includes a mock fetch so the example runs offline with node, plus the real-API version commented in.

## Code

See [`fetch_api.js`](fetch_api.js) in this folder, with tests.

```javascript
async function loadUsers(fetchFn) {
  try {
    const response = await fetchFn("https://jsonplaceholder.typicode.com/users");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const users = await response.json();
    return users.map(u => `${u.name} <${u.email}>`);
  } catch (err) {
    return [`Error: ${err.message}`];
  }
}
```

## Example

`loadUsers(mockFetch)` returns names and emails; with a failing mock it returns an error string instead of crashing.

## Next

SQL SELECT / JOIN: pull the right rows from two tables in one query.
