CREATE DATABASE IF NOT EXISTS xyz;

CREATE TABLE IF NOT EXISTS employee_info (
	id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
    );
    
INSERT INTO employee_info
	(id, name, salary)
    VALUES
    (1, "Adam", 25000),
    (2, "bob", 30000),
    (3, "casey", 40000);
    
SELECT * FROM employee_info;