# DATABASE QUESTION 5

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0178",
    database="school"
)

if connection.is_connected():
    print("Connected to MySQL Database")

    cursor = connection.cursor()

    s_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")

    query = '''
    INSERT INTO students (student_id, name, age, grade)
    VALUES ({}, '{}', {}, '{}')
    '''.format(s_id, name, age, grade)

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

else:
    print("Failed to connect to the database.")
