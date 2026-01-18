--Part-3: Performing CRUD Operations in Online Bookstore.

--Insert a new author and a new book by that author.
INSERT INTO Authors (name, country)
VALUES ('Robert Kiyosaki', 'USA');

INSERT INTO Books (title, author_id, price, stock)
VALUES ('Rich Dad Poor Dad', 6, 450.00, 20);

--Update the price of a book.
UPDATE Books
SET price = 690.00
WHERE title = 'Harry Potter 1';

--Delete a customer from the database.
DELETE FROM Orders WHERE customer_id = 3;
DELETE FROM Customers WHERE customer_id = 3;

--Insert a new order for a customer.
INSERT INTO Orders (customer_id, book_id, quantity, order_date)
VALUES (1, 2, 1, CONVERT(DATE, GETDATE()));
