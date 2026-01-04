--9.Write an SQL query to find employees who do not have any records in the Attendance table.

CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,
    emp_id INT,
    date DATE
);

INSERT INTO Attendance VALUES
(1,1,'2026-01-01'),
(2,2,'2026-01-01'),
(3,3,'2026-01-01');

--Answer:
SELECT e.name
FROM Employees e
LEFT JOIN Attendance a
ON e.emp_id = a.emp_id
WHERE a.emp_id IS NULL;
