--8.Given a table Customers(customer_id, customer_name, city), write a query to find cities that have more than 5 customers.

CREATE TABLE Customers (
    customer_id INT NOT NULL IDENTITY PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO Customers VALUES
('Ravinder','Hyderabad'),
('Arun','Hyderabad'),
('Kumar','Hyderabad'),
('Swathi','Bengluru'),
('Neel','Hyderabad'),
('Ravi','Hyderabad'),
('Raju','Hyderabad'),
('Anushka','Chennai');

SELECT city, COUNT(*) AS Customer_Count
FROM Customers
GROUP BY city
HAVING COUNT(*) > 5;
