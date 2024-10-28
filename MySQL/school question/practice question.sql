CREATE DATABASE school;

USE school;

/*                  QUESTION 2                 */
CREATE TABLE Furniture (
    No INT,
    Itemname VARCHAR(50),
    Type VARCHAR(50),
    Dateofstock DATE,
    Price DECIMAL(10, 2),
    Discount INT
);

INSERT INTO Furniture 
(No, Itemname, Type, Dateofstock, Price, Discount) 
VALUES
(1, 'White lotus', 'Double Bed', '2002-02-23', 30000, 25),
(2, 'Pink feather', 'Baby Cot', '2002-01-20', 7000, 20),
(3, 'Dolphin', 'Baby Cot', '2002-02-19', 9500, 20),
(4, 'Decent', 'Office Table', '2002-01-01', 25000, 30),
(5, 'Comfort Zone', 'Double Bed', '2002-01-12', 25000, 25),
(6, 'Donald', 'Baby Cot', '2002-02-24', 6500, 15),
(7, 'Royal finish', 'Office Table', '2002-02-20', 18000, 30),
(8, 'Royal tiger', 'Sofa', '2002-02-22', 31000, 30),
(9, 'Econo sitting', 'Sofa', '2001-12-13', 9500, 25),
(10, 'Paradise', 'Dining Table', '2002-02-19', 11500, 25),
(11, 'Wood Comfort', 'Double Bed', '2003-03-23', 25000, 25),
(12, 'Old Fox', 'Sofa', '2003-02-20', 17000, 20),
(13, 'Micky', 'Baby Cot', '2003-02-21', 7500, 15);

SELECT Itemname 
FROM Furniture 
WHERE Type="Double Bed";

SELECT MONTHNAME(Dateofstock) 
FROM Furniture 
WHERE Type="Sofa";

SELECT Price*Discount 
FROM Furniture 
WHERE Dateofstock > 2002/12/31 ;

/*                  QUESTION 3                */

CREATE TABLE games (
    GCode INT PRIMARY KEY,
    GameName VARCHAR(50),
    Number INT,
    PrizeMoney DECIMAL(10, 2),
    ScheduleDate DATE
);

INSERT INTO games 
(GCode, GameName, Number, PrizeMoney, ScheduleDate) 
VALUES
(101, 'Carom Board', 2, 5000, '2004-01-23'),
(102, 'Badminton', 2, 12000, '2003-12-12'),
(103, 'Table Tennis', 4, 8000, '2004-02-14'),
(105, 'Chess', 2, 9000, '2004-01-01'),
(108, 'Lawn Tennis', 4, 25000, '2004-03-19');

SELECT COUNT(DISTINCT Number) 
FROM GAMES;

SELECT MAX(ScheduleDate),MIN(ScheduleDate) 
FROM GAMES;

SELECT SUM(PrizeMoney) 
FROM GAMES;


/*                  QUESTION 4                  */

CREATE TABLE detergents (
    PID INT PRIMARY KEY,
    PName VARCHAR(50),
    Price DECIMAL(10, 2),
    Category VARCHAR(50),
    Manufacturer VARCHAR(50)
);

INSERT INTO detergents 
(PID, PName, Price, Category, Manufacturer) 
VALUES
(1, 'Nirma', 40, 'Detergent Powder', 'Nirma Group'),
(2, 'Surf', 80, 'Detergent Powder', 'HL'),
(3, 'Vim Bar', 20, 'Disc washing Bar', 'HL'),
(4, 'Neem Face Wash', 50, 'Face Wash', 'Himalaya');

SELECT *
FROM detergents
WHERE manufacturer <> 'HL';

SELECT  pname
FROM detergents
WHERE manufacturer = 'HL';

SELECT pname 
FROM detergents 
WHERE price > 50;

SELECT pname 
FROM detergents
WHERE pname LIKE 'N%';

/*                  QUESTION 5                  */

#SELECT NAME,SAL,DESIGNATION WHERE DISCOUNT=NULL;
/*
SELECT NAME, SAL, DESIGNATION 
FROM employees 
WHERE DISCOUNT IS NULL;
*/

/*                  QUESTION 6                  */

CREATE TABLE sports (
    Rno INT PRIMARY KEY,
    Class INT,
    Name VARCHAR(50),
    Game VARCHAR(50),
    Grade CHAR(1),
    Marks INT
);

INSERT INTO sports 
(Rno, Class, Name, Game, Grade, Marks) 
VALUES
(10, 7, 'Sameer', 'Cricket', 'B', 61),
(11, 8, 'Sujit', 'Tennis', 'A', 75),
(12, 7, 'Kamal', 'Swimming', 'B', 60),
(13, 9, 'Veena', 'Tennis', 'C', 49),
(15, 10, 'Arpit', 'Cricket', 'A', 78);

SELECT game, count(*) 
FROM sports GROUP BY game;

SELECT max(marks), min(marks) 
FROM sports;

SELECT DISTINCT game 
FROM sports;

SELECT name , game, marks 
FROM sports WHERE marks BETWEEN 60 AND 75;

/*                  QUESTION 7                  */

CREATE TABLE doctor (
    DID INT PRIMARY KEY,
    DName VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Date_of_join DATE,
    Salary DECIMAL(10, 2),
    Gender CHAR(1)
);

INSERT INTO doctor 
(DID, DName, Age, Department, Date_of_join, Salary, Gender) 
VALUES
(1, 'Rakesh', 34, 'General', '2017-01-10', 120000, 'M'),
(2, 'Parveen', 31, 'Ortho', '2008-03-24', 200000, 'F'),
(3, 'Satyajeet', 32, 'ENT', '2016-12-12', 300000, 'M'),
(4, 'Yogita', 35, 'Heart', '2015-07-01', 400000, 'F'),
(5, 'Chirag', 42, 'General', '2007-09-05', 250000, 'M'),
(6, 'Vijay', 50, 'ENT', '2008-06-27', 300000, 'M'),
(7, 'Kamlesh', 44, 'Ortho', '2017-02-25', 210000, 'M'),
(8, 'Seema', 33, 'Heart', '2018-07-31', 200000, 'F');

CREATE TABLE place (
    PID INT PRIMARY KEY,
    Department VARCHAR(50),
    City VARCHAR(50)
);

INSERT INTO place 
(PID, Department, City) 
VALUES
(1, 'General', 'Ajmer'),
(2, 'Heart', 'Udaipur'),
(3, 'Ortho', 'Jodhpur'),
(4, 'ENT', 'Jaipur');

SELECT department, count(*) 
FROM doctor 
GROUP BY department;

SELECT Max(salary), Min(salary), Max(date_of_join ) 
FROM doctor; 

SELECT doctor.dname, doctor.department, place.city
FROM doctor, place 
WHERE doctor.department = place.department 
	AND place.city IN ("Jaipur", "Jodhpur");


