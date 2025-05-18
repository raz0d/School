import mysql.connector as mycon

connection = mycon.connect(
    host="localhost",
    user="root",
    password="0178",
    database="boards"
)

if connection.is_connected():
    print("connection is established")
    cursor = connection.cursor()
    query = '''
        CREATE TABLE today(
            id INT PRIMARY KEY,
            name VARCHAR(50)
        );
    '''
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
else:
    print("connection not established")