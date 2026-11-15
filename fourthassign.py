SELECT customers.name, orders.item
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
WHERE customers.city = 'Pune'
ORDER BY customers.name ASC, orders.item ASC;


SELECT customers.name, customers.city
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
WHERE orders.customer_id IS NULL
ORDER BY customers.name ASC;


SELECT orders.id, orders.item, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id
WHERE customers.id IS NULL
ORDER BY orders.amount ASC;


SELECT customers.name, orders.item, orders.amount
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
ORDER BY customers.name ASC, orders.amount ASC;
