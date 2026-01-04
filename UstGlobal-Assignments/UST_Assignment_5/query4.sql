--4.Given tables Students(student_id, name) and Marks(student_id, subject, marks), write a query to find students
--who have scored more than 80 in at least two subjects.

CREATE TABLE Students (
    student_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO Students VALUES
(101,'Raju'),
(102,'Arun'),
(103,'Bharath'),
(104,'Vignesh'),
(105,'Vinay');

CREATE TABLE Marks (
    student_id INT NOT NULL,
    subject VARCHAR(30),
    marks INT
);

INSERT INTO Marks VALUES
(101,'Maths',85),
(101,'Science',90),
(102,'Maths',78),
(102,'Science',88),
(103,'Maths',92),
(103,'English',95),
(104,'Science',82),
(104,'Maths',92),
(105,'Science',72),
(105,'English',75);


-- Answer:
SELECT student_id, name
FROM Students
WHERE student_id IN (
    SELECT student_id
    FROM Marks
    WHERE marks > 80
    GROUP BY student_id
    HAVING COUNT(DISTINCT subject) >= 2
);

