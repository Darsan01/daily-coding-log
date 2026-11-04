// Day 10 — Fetch API: fetch and render JSON (JavaScript).
//
// fetch() returns a Promise of a Response, not the data itself:
// await response.json() to parse it. fetch only rejects on network
// failure — a 404/500 still resolves, so check response.ok first.
// Track three states: loading, data, error.

async function loadUsers(fetchFn) {
  try {
    const response = await fetchFn("https://jsonplaceholder.typicode.com/users");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const users = await response.json();
    return users.map((u) => `${u.name} <${u.email}>`);
  } catch (err) {
    return [`Error: ${err.message}`];
  }
}

// Mock fetch implementations so the example runs offline with node.
function mockFetchOk() {
  return Promise.resolve({
    ok: true,
    status: 200,
    json: () =>
      Promise.resolve([
        { name: "Leanne Graham", email: "Sincere@april.biz" },
        { name: "Ervin Howell", email: "Shanna@melissa.tv" },
      ]),
  });
}

function mockFetch404() {
  return Promise.resolve({ ok: false, status: 404, json: () => Promise.resolve({}) });
}

function mockFetchDown() {
  return Promise.reject(new Error("Network down"));
}

// Real-API version (needs network; uncomment to try it):
// loadUsers(fetch).then(console.log);

async function runTests() {
  const assert = require("node:assert");
  let got = await loadUsers(mockFetchOk);
  assert.deepStrictEqual(got, ["Leanne Graham <Sincere@april.biz>", "Ervin Howell <Shanna@melissa.tv>"]);
  console.log("PASS: success path renders names + emails");
  got = await loadUsers(mockFetch404);
  assert.deepStrictEqual(got, ["Error: HTTP 404"]);
  console.log("PASS: 404 becomes an error string, not a crash");
  got = await loadUsers(mockFetchDown);
  assert.deepStrictEqual(got, ["Error: Network down"]);
  console.log("PASS: network failure becomes an error string, not a crash");
  console.log("\n3/3 tests passed");
}

if (require.main === module) {
  runTests();
}

module.exports = { loadUsers };
