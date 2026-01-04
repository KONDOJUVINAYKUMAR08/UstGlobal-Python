--2.Given a table Orders(order_id, customer_id, order_date, amount), write a query to find the total order amount per customer, 
--  but display only customers whose total exceeds 50,000.

CREATE TABLE Orders (
    order_id INT NOT NULL IDENTITY PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO Orders VALUES
(101,'2025-10-10',25000),
(101,'2025-12-12',15000),
(102,'2026-01-02',85000),
(103,'2026-01-01',60000),
(104,'2026-01-02',40000);

-- Answer:

SELECT customer_id, SUM(amount) AS Total_Amount
FROM Orders
GROUP BY customer_id
HAVING SUM(amount) > 50000;

