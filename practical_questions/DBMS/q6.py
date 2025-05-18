import mysql.connector as con

connection = con.connect(
    host="localhost",
    user="root",
    password="0178",
    database="boards"
)

if connection.is_connected():
    cursor = connection.cursor()

    query = '''
        SELECT * FROM students
    '''
    cursor.execute(query)
    records_1 = cursor.fetchone()
    print(records_1)
    record_2 = cursor.fetchmany(2)
    print(record_2)
    record_3 = cursor.fetchall()
    print(record_3)
    cursor.close()
    connection.close()
else:
    print("connection not connected")