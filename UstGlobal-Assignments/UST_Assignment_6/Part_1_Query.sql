-- PART-1: Creating Tables required for Online Bookstore

--Creating Database.

CREATE DATABASE OnlineBookstore;
USE OnlineBookstore;


--Authors Table
CREATE TABLE Authors (
    author_id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

--Books Table
CREATE TABLE Books (
    book_id INT IDENTITY PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author_id INT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

--Customers Table
CREATE TABLE Customers (
    customer_id INT IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

--Orders Table
CREATE TABLE Orders (
    order_id INT IDENTITY PRIMARY KEY,
    customer_id INT,
    book_id INT,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
