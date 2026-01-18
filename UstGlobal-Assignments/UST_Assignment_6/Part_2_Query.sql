--Part-2: Insert Sample Data in tables for online bookstore.

--Inserting Authors.
INSERT INTO Authors (name, country) VALUES
('J.K. Rowling', 'UK'),
('George R.R. Martin', 'USA'),
('Chetan Bhagat', 'India'),
('Paulo Coelho', 'Brazil'),
('Dan Brown', 'USA');

--Inserting Books.
INSERT INTO Books (title, author_id, price, stock) VALUES
('Harry Potter 1', 1, 499.00, 10),
('Harry Potter 2', 1, 550.00, 8),
('Game of Thrones', 2, 799.00, 5),
('Clash of Kings', 2, 850.00, 3),
('2 States', 3, 299.00, 15),
('Half Girlfriend', 3, 320.00, 2),
('The Alchemist', 4, 399.00, 12),
('Brida', 4, 350.00, 6),
('Da Vinci Code', 5, 599.00, 4),
('Angels and Demons', 5, 620.00, 1);

--Inserting Customers.
INSERT INTO Customers (name, email) VALUES
('Vinay Kumar', 'vinay@gmail.com'),
('Vignesh', 'vignesh@gmail.com'),
('Bharath', 'bharath@gmail.com');

--Inserting Orders.
INSERT INTO Orders (customer_id, book_id, quantity, order_date) VALUES
(1, 1, 2, '2026-01-10'),
(1, 3, 1, '2026-01-12'),
(2, 5, 3, '2026-01-15'),
(2, 7, 1, '2026-01-17'),
(3, 9, 2, '2026-01-18'),
(3, 4, 2, '2026-01-18');