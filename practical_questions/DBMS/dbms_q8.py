import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="school"
)

if connection.is_connected():
    print("Connected to MySQL Database")

    cursor = connection.cursor()

    student_id = int(input("Enter the Student ID of the record to delete: "))

    query = '''
    DELETE FROM students
    WHERE student_id = {}
    '''.format(student_id)

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

else:
    print("Failed to connect to the database.")
