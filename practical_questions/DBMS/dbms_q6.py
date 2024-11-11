# DATABASE QUESTION 6

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

    query = "SELECT * FROM students"
    cursor.execute(query)

    print("Fetching one record using fetchone():")
    record = cursor.fetchone()
    print(record)

    print("\nFetching two records using fetchmany(2):")
    records = cursor.fetchmany(2)
    for row in records:
        print(row)

    print("\nFetching all remaining records using fetchall():")
    all_records = cursor.fetchall()
    for row in all_records:
        print(row)

    cursor.close()
    connection.close()

else:
    print("Failed to connect to the database.")
