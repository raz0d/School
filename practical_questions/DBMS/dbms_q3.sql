#1. SUM()
SELECT SUM(age) AS total_age 
FROM school_students;

#2. AVG()
SELECT AVG(age) AS average_age 
FROM school_students;

#3. MIN()
SELECT MIN(age) AS youngest_student 
FROM school_students;

#4. MAX()
SELECT MAX(age) AS oldest_student 
FROM school_students;

#5. COUNT()

#5.1 Counting all rows:
SELECT COUNT(*) AS total_students 
FROM school_students;

#5.2 Counting specific values:
SELECT COUNT(grade) AS students_with_grades 
FROM school_students WHERE grade IS NOT NULL;

# Combining Aggregate Functions with GROUP BY
SELECT grade, COUNT(*) AS students, AVG(age) AS avg_age
FROM school_students
GROUP BY grade;
