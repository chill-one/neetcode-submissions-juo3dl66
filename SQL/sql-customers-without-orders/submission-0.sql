-- Write your query below
SELECT c.name
FROM customers c
WHERE NOT EXISTS (
    SELECT c.name
    FROM customers
    JOIN orders o on o.customer_id = c.id
);