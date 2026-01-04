--5.Write an SQL query to retrieve the names of employees who earn more than the average salary of their department.

SELECT e.name
FROM Employees e
WHERE e.salary >
(
    SELECT AVG(salary)
    FROM Employees
    WHERE dept_id = e.dept_id
);