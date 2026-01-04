--6.Given a table Sales(sale_id, product_id, sale_date, quantity), write a query to find the total quantity sold for each product 
--in the year 2024.

CREATE TABLE Sales (
    sale_id INT NOT NULL IDENTITY PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT
);


INSERT INTO Sales VALUES
(1001,'2024-10-05',10),
(1001,'2024-03-15',20),
(1002,'2023-12-10',15),
(1002,'2024-06-18',30),
(1003,'2024-11-10',50),
(1003,'2025-01-18',35);

--Answer:
SELECT product_id, SUM(quantity) AS Total_Quantity
FROM Sales
WHERE YEAR(sale_date) = 2024
GROUP BY product_id;
