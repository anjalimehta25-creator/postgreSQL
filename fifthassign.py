SELECT customers.city, SUM(orders.amount) AS total
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.city
ORDER BY total DESC;


SELECT item,
COUNT(*) AS num_orders,
SUM(amount) AS total
FROM orders
GROUP BY item
ORDER BY num_orders DESC, item ASC;
