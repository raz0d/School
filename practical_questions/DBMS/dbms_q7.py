# DATABASE QUESTION 7

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

    student_id = int(input("Enter Student ID to update: "))
    new_grade = input("Enter the new grade: ")

    query = '''
    UPDATE students
    SET grade = '{}'
    WHERE student_id = {}
    '''.format(new_grade, student_id)

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

else:
    print("Failed to connect to the database.")
