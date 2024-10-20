USE my_db;

CREATE TABLE stud (
	rollno INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(20)
);

INSERT INTO stud
	(rollno, name, marks, grade, city)
    VALUES
    (101, "anil", 78, "C", "Pune"),
    (102, "bhumika", 93, "A", "Mumbai"),
    (103, "chetan", 85, "B", "Mumbai"),
    (104, "dhruv", 96, "A", "Delhi"),
    (105, "emanuel", 12, "F", "Delhi"),
    (106, "farah", 82, "B", "Delhi");
    
SELECT * FROM stud;

ALTER TABLE stud
	CHANGE COLUMN name full_name VARCHAR(50);
    
DELETE FROM stud
	WHERE marks<80;
    
ALTER TABLE stud
	DROP COLUMN grade;
    