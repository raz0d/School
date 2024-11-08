#1 Creating a Database
CREATE DATABASE school;

#2 Showing All Databases
SHOW DATABASES;

#3 Using a Database
USE school;

#4 Creating a Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);

#5 Showing All Tables in a Database
SHOW TABLES;

#6 Describing Table Structure
DESCRIBE students;

#7 Renaming a Table
RENAME TABLE students 
TO school_students;

#8 Altering a Table

#8.1 Adding a Column:
ALTER TABLE school_students 
ADD COLUMN address VARCHAR(100);

#8.2 Modifying a Column:
ALTER TABLE school_students 
MODIFY COLUMN age SMALLINT;

#8.3 Dropping a Column:
ALTER TABLE school_students 
DROP COLUMN address;

#9 Inserting Data into a Table
INSERT INTO school_students 
(student_id, name, age, grade)
VALUES 
(1, 'John Doe', 17, '12th');

#10 Selecting Data from a Table

#10.1 Basic Select:
SELECT * FROM school_students;

#10.2 With Specific Columns:
SELECT name, grade 
FROM school_students;

#10.3 With a Condition:
SELECT * FROM school_students 
WHERE grade = '12th';

#11 Updating Data in a Table
UPDATE school_students
SET age = 18
WHERE student_id = 1;
























