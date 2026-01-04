--1.Write an SQL query to display the second highest salary from an Employees table.

CREATE TABLE Employees (
    emp_id INT NOT NULL IDENTITY PRIMARY KEY,
    name VARCHAR(60),
    age INT,
    salary INT,
    dept_id INT,
    manager_id INT,
);

INSERT INTO Employees VALUES
('Arun',34,80000,10,1),
('Ravi',45,60000,10,1),
('Swathi',24,90000,20,2),
('Kiran',27,55000,10,1),
('Niharika',36,95000,20,2),
('Pooja',42,50000,30,4),
('Arjun',28,52000,30,4);

-- Answer:
SELECT MAX(salary) AS Second_Highest_Salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);