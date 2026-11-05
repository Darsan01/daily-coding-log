# Day 11 — 2026-11-04

## Topic: SQL practice — SELECT / JOIN (SQL)


**Problem:** Given two tables — `customers (id, name, city)` and `orders (id, customer_id, total, created_at)` — write queries to: list every order with its customer's name, find customers with no orders, and rank customers by total spend.

## What I learned

- INNER JOIN keeps only matching rows; LEFT JOIN keeps every row from the left table and fills in NULL where there is no match. 'Customers with no orders' is a LEFT JOIN plus `WHERE orders.id IS NULL` — a pattern that shows up in interviews constantly.
- Filter rows with WHERE, filter groups with HAVING: `HAVING SUM(total) > 100` works after GROUP BY, while `WHERE SUM(total) > 100` is an error because aggregates don't exist yet at the WHERE stage.
- GROUP BY + an aggregate (SUM, COUNT, AVG) turns rows into summaries — one row per customer with their total spend, ordered with ORDER BY … DESC and capped with LIMIT for a top-N list.
- An index on the join key (`orders.customer_id`) is what keeps a JOIN fast as tables grow; without it the database scans the whole orders table for every customer.

## Code

See [`queries.sql`](queries.sql) in this folder, with tests.

```sql
-- Every order with its customer's name
SELECT o.id, c.name, o.total, o.created_at
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id;

-- Customers with no orders
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.id = c.id
WHERE o.id IS NULL;
```

## Example

Top spender query: `SELECT c.name, SUM(o.total) AS spend FROM customers c JOIN orders o ON o.id = c.id GROUP BY c.id ORDER BY spend DESC LIMIT 3;` — the .sql file also creates the tables with sample rows so the queries can be run as-is in SQLite.

## Next

PHP form handling with validation: never trust user input.
