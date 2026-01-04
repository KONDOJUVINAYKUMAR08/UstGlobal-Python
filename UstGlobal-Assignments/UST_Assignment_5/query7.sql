--7.Write an SQL query to display the top 3 highest-paid employees from each department.

SELECT *
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM Employees
) e
WHERE rnk <= 3;
