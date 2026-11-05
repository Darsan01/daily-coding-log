-- Day 11 — SQL practice: SELECT / JOIN (SQLite-compatible).
--
-- Two tables: customers (id, name, city) and orders (id, customer_id,
-- total, created_at). Run the whole file in sqlite3: it creates the
-- tables, inserts sample rows, then runs the queries.

CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(id),
  total REAL,
  created_at TEXT
);

INSERT INTO customers VALUES
  (1, 'Asha', 'Kathmandu'),
  (2, 'Bikash', 'Pokhara'),
  (3, 'Mina', 'London'),
  (4, 'Rohan', 'London');
INSERT INTO orders VALUES
  (1, 1, 45.00, '2026-10-01'),
  (2, 1, 120.50, '2026-10-12'),
  (3, 2, 30.00, '2026-10-05'),
  (4, 3, 250.00, '2026-10-20');

-- 1. Every order with its customer's name (INNER JOIN: only matches).
SELECT o.id, c.name, o.total, o.created_at
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id;

-- 2. Customers with no orders (LEFT JOIN + NULL check).
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- 3. Total spend per customer (GROUP BY + SUM), top spenders first.
SELECT c.name, SUM(o.total) AS spend
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id
ORDER BY spend DESC;

-- 4. Big spenders only (HAVING filters groups, not rows).
SELECT c.name, SUM(o.total) AS spend
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id
HAVING spend > 100;

-- 5. Customers in London, alphabetically.
SELECT name FROM customers WHERE city = 'London' ORDER BY name;
