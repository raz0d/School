-- DATABASE QUESTION 2

#1. Using DISTINCT
SELECT DISTINCT grade 
FROM school_students;

#2. Using BETWEEN
SELECT * FROM school_students 
WHERE age BETWEEN 15 AND 18;

#3. Using IN
SELECT * FROM school_students 
WHERE grade IN ('10th', '12th');

#4. Using LIKE
 -- Names starting with 'J'
SELECT * FROM school_students 
WHERE name LIKE 'J%'; 

-- names with exactly two characters before "son"
SELECT * FROM school_students 
WHERE name LIKE '__son';

#5. Using IS NULL
SELECT * FROM school_students 
WHERE address IS NULL;

#6. Using ORDER BY
SELECT * FROM school_students 
ORDER BY age ASC;  -- Ascending order
SELECT * FROM school_students 
ORDER BY grade DESC, age ASC;  -- Multiple columns

#7. Using GROUP BY
SELECT grade, COUNT(*) AS total_students
FROM school_students
GROUP BY grade;

#8. Using HAVING
SELECT grade, COUNT(*) AS total_students
FROM school_students
GROUP BY grade
HAVING COUNT(*) > 10; 













