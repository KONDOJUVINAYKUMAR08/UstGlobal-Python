--3.Write an SQL query to find the number of employees in each department, excluding departments with fewer than 3 employees.

SELECT dept_id, COUNT(*) AS employee_count
FROM Employees
GROUP BY dept_id
HAVING COUNT(*) >= 3;
