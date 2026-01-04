--10.Given a table Employees(employee_id, name, manager_id), write an SQL query to display each employee’s name along with
--their manager’s name.
CREATE TABLE Managers(
    manager_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO Managers VALUES
(1,'Ravinder'),
(2,'Vanshika'),
(3,'Vinay'),
(4,'Vamsi');

--Answer:
SELECT e.name AS Employee_name,
       m.name AS Manager_name
FROM Employees e
LEFT JOIN Managers m
ON e.manager_id = m.manager_id;