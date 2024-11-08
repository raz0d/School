# QUESTION 4

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

    create_table_query = '''
    CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        grade VARCHAR(10)
    );
    '''

    try:
        cursor.execute(create_table_query)
        print("Table 'students' created successfully in the database.")
    except mysql.connector.Error:
        print("Error")

    cursor.close()
    connection.close()
    print("MySQL connection is closed.")

else:
    print("Failed to connect to the database.")
