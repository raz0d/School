 # CREATE AND DELETE DB
CREATE DATABASE my_db;
CREATE DATABASE IF NOT EXISTS my_db;

DROP DATABASE IF EXISTS company;

# USING A DB
USE my_db;

# CREATING TABLE
CREATE TABLE IF NOT EXISTS stud_det (
		id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT NOT NULL
);

INSERT INTO stud_det (id, name, age) VALUES(1, "Alsamad", 19);
INSERT INTO stud_det (name, age, id) VALUES("Tabassum", 18, 2);

SELECT * FROM stud_det ;

# SHOW 
SHOW DATABASES;
SHOW TABLES;

# INSERT INTO
INSERT INTO stud_det
	(age, name, id)
	VALUES
	(17, "Ansh", 3),
    (17, "Anuj", 4),
    (12, "Aditya", 5);
   
/*               CONSTRAINT               */

# NOT NULL
CREATE TABLE temp1 (
	id INT NOT NULL
);
INSERT INTO temp1 VALUES(1);
INSERT INTO temp1 VALUES(NULL); # ERROR
INSERT INTO temp1 VALUES(1); # NO ERROR

# UNIQUE
CREATE TABLE temp2 (
	id INT UNIQUE
);
INSERT INTO temp2 VALUES(1);
INSERT INTO temp2 VALUES(NULL); # NO ERROR
INSERT INTO temp2 VALUES(1); # ERROR

# PRIMARY KEY
CREATE TABLE temp3 (
	id INT,
    name VARCHAR(50),
    salary INT,
    PRIMARY KEY (id, name) # ID & NAME CANT BE SAME SIMULTANEOUSLY 
);

# DEFAULT
CREATE TABLE temp4 (
	id INT,
    salary INT DEFAULT 25000
);
INSERT INTO temp4 (id) VALUES(101);
SELECT * FROM temp4;

# CHECK 
CREATE TABLE temp5 (
	id INT,
	name VARCHAR(50),
    city VARCHAR(50),
    age INT,
    CONSTRAINT age_limit CHECK ( age >= 18 AND city = "Delhi")
);
INSERT INTO temp5 VALUES (101, "Alsamad", "Delhi", 19);
INSERT INTO temp5 VALUES (102, "Tabassum", "Gorakhpur", 18); # ERROR
INSERT INTO temp5 VALUES (103, "Ansh", "Delhi", 17); # ERROR
SELECT * FROM temp5;

CREATE TABLE temp6 (
	name VARCHAR(50),
    age INT CHECK (age >= 18)
);
INSERT INTO temp6 VALUES ("Alsamad", 19);
INSERT INTO temp6 VALUES ("Ansh", 17); # ERROR

# TEST TABLE 
CREATE TABLE student (
	rollno INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(20)
);

INSERT INTO student
	(rollno, name, marks, grade, city)
    VALUES
    (101, "anil", 78, "C", "Pune"),
    (102, "bhumika", 93, "A", "Mumbai"),
    (103, "chetan", 85, "B", "Mumbai"),
    (104, "dhruv", 96, "A", "Delhi"),
    (105, "emanuel", 12, "F", "Delhi"),
    (106, "farah", 82, "B", "Delhi");
    

/*        SOME COMMANDS          */

# SELECT 
SELECT grade, name FROM student;
SELECT * FROM student;
SELECT DISTINCT city FROM student; 

#WHERE 
SELECT name FROM student WHERE marks > 90; # students names with 90+ marks
SELECT * FROM student WHERE city = "Pune";

# OPERATORS 

# AND
SELECT name, rollno, marks, city
	FROM student
	WHERE marks > 80 AND city = "Delhi";
    
# OR
SELECT name, rollno, marks, city
	FROM student
	WHERE marks > 80 OR city = "Delhi";
    
# MODULUS
SELECT *
	FROM student
    WHERE marks % 2 = 0 ;
    
# BETWEEN
SELECT *
	FROM student
    WHERE marks BETWEEN 80 AND 90; # 80 & 90 included

# IN
SELECT *
	FROM student
    WHERE city IN ("Delhi", "Pune", "Gurgaon");

# NOT IN 
SELECT *
	FROM student
    WHERE city NOT IN ("Delhi", "Pune");
    
# LIMIT
SELECT name, marks, rollno, city
	FROM student
    WHERE rollno > 101 AND marks BETWEEN 70 AND 100
    AND city IN ("Mumbai", "Pune", "Gorakhpur")
    LIMIT 3;
    
# ORDER BY (by default ASC)
SELECT *
	FROM student
    WHERE marks BETWEEN 70 AND 90 
    AND grade IN ("A","B", "F")
    ORDER BY city ASC
    LIMIT 3;

SELECT * # DATA OF TOP 3 STUDENTS
	FROM student
    ORDER BY marks DESC
    LIMIT 3;

# AGGREGATE FUNCTIONS

# COUNT
SELECT COUNT(name) FROM student; 
SELECT COUNT(marks) FROM student; 

# MAX
SELECT MAX(marks) FROM student; 
SELECT MAX(name) FROM student;

# MIN
SELECT MIN(marks) FROM student;
SELECT MIN(name) FROM student;

# SUM
SELECT SUM(marks) FROM student;

# AVG
SELECT AVG(marks) FROM student;

# GROUP BY CLAUSE
SELECT city, COUNT(rollno) # no. of students per city
	FROM student
    GROUP BY city;

SELECT city, name, COUNT(rollno)
	FROM student
    GROUP BY city, name;

SELECT city, AVG(marks) # avg marks per city
	FROM student
    GROUP BY city;

SELECT grade, COUNT(rollno) as "no of students"
	FROM student
    GROUP BY grade
    ORDER BY grade;

# HAVING CLAUSE (simply where condition on groups kinda)
SELECT city, COUNT(rollno) # no of students in each city where max marks crossed 90
	FROM student
    GROUP BY city
    HAVING MAX(marks) > 90;

# UPDATE COMMAND (to update existing row)

CREATE TABLE temp7 (
	rno INT PRIMARY KEY,
    name VARCHAR(50),
    grade VARCHAR(1)
);
INSERT INTO temp7 
	(rno, name, grade)
    VALUES
    (101, "Alsamad", "A"),
    (102, "Tabassum", "B"),
    (103, "Ansh", "B"),
    (104, "Anuj", "C"),
    (105, "Badmosh", "A");

SET SQL_SAFE_UPDATES = 0;

UPDATE temp7 
	SET grade = "O"
    WHERE grade = "A";
UPDATE temp7
	SET grade = "A"
    WHERE rno = 102;
UPDATE temp7
	SET rno = rno + 15;
    
SELECT * FROM temp7;

# DELETE COMMAND (delete existing row )

DELETE FROM temp7
	WHERE grade = "C";
DELETE FROM temp7; # PURA TABLE KA DATA KHTM HO JAYEGA

# FOREIGN KEY

# PARENT TABLE
CREATE TABLE dept (
	id INT PRIMARY KEY,
    name VARCHAR(50)
);

# CHILD TABLE
CREATE TABLE teacher (
	id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES dept(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

INSERT INTO dept
	(id, name)
    VALUES
    (101, "Science"),
    (102, "English"),
    (103, "Hindi");
    
SELECT * FROM dept;

INSERT INTO teacher
	(id, name, dept_id)
    VALUES
    (101, "Adam", 101),
    (102, "Bob", 103),
    (103, "Casey", 102),
    (104, "Donald", 102);
    
SELECT * FROM teacher;

UPDATE dept
	SET id = 67
    WHERE name = "English";

DELETE FROM dept
	WHERE id = 103;

# ALTER COMMMANDS

# ADD COLUMN
ALTER TABLE student
	ADD COLUMN age INT DEFAULT 19;
    
# DROP COLUMN
ALTER TABLE student
	DROP COLUMN age;
    
# RENAME TABLE
ALTER TABLE student
	RENAME TO student_details;
    
ALTER TABLE student_details
	RENAME TO student;
    
# MODIFY TABLE (modify datatypes / constraint)
ALTER TABLE student
	MODIFY COLUMN age VARCHAR(2);
    
# CHANGE TABLE (rename / change data types)
ALTER TABLE student
	CHANGE COLUMN age stud_age INT;

# TRUNCATE COMMAND (delets all records from the table not the table)

TRUNCATE TABLE student;

SELECT * FROM student;

/*            JOINS              */

CREATE TABLE temp_student (
	student_id INT PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE temp_course (
	student_id INT PRIMARY KEY,
    course VARCHAR(50)
);
INSERT INTO temp_student
	(student_id, name)
    VALUES
    (101, "Adam"),
    (102, "Bob"),
    (103, "Casey");
INSERT INTO temp_course
	(student_id , course)
    VALUES
    (102, "English"),
    (105, "Math"),
    (103, "Science"),
    (107, "Computer Science");
SELECT * FROM temp_student; 
SELECT * FROM temp_course;

# INNER JOINS
SELECT *
	FROM temp_student as s
    INNER JOIN temp_course as c
    ON s.student_id = c.student_id;

# LEFT JOIN
SELECT *
	FROM temp_student as s
    LEFT JOIN temp_course as c
    ON s.student_id = c.student_id;

# RIGHT JOIN
SELECT *
	FROM temp_student as a
    RIGHT JOIN temp_course as b
    ON a.student_id = b.student_id;

# LEFT EXCLUSIVE 
SELECT *
	FROM temp_student as a
    LEFT JOIN temp_course as b
    ON a.student_id = b.student_id
    WHERE b.student_id IS NULL;
    
# RIGHT EXCLUSIVE
SELECT *
	FROM temp_student as a
    RIGHT JOIN temp_course as b
    ON a.student_id = b.student_id
    WHERE a.student_id IS NULL;
    
# FULL JOIN 
SELECT * 
	FROM temp_student as a
    LEFT JOIN temp_course as b
	ON a.student_id = b.student_id
UNION
SELECT*
	FROM temp_student as a
    RIGHT JOIN temp_course as b
    ON a.student_id = b.student_id;
	
    
# FULL EXCLUSIVE JOIN (RIGHT EXCLUSIVE + LEFT EXCLUSIVE)alter
SELECT *
	FROM temp_student as a
	LEFT JOIN temp_course as b
	ON a.student_id = b.student_id
    WHERE b.student_id IS NULL
UNION
SELECT *
	FROM temp_student as a
	RIGHT JOIN temp_course as b
	ON a.student_id = b.student_id
	WHERE a.student_id IS NULL;
    
# SELF JOIN (1 table ko usi se join krdega)










