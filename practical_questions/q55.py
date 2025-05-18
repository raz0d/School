import mysql.connector as con

connection = con.connect(
    host="localhost",
    user="root",
    passwd="0178",
    database="boards"
)

if connection.is_connected():
    print("connection successful")
    cursor = connection.cursor()
    ans = "y"
    while ans == "y":
        id_ = int(input("enter id: "))
        name_ = input("enter name: ")
        query = '''
            INSERT INTO today
            (id, name)
            VALUES
            (%s, %s);
        '''
        cursor.execute(query, (id_, name_))
        ans = input("add more records (y/n): ")
    connection.commit()

    cursor.close()
    connection.close()
else:
    print("connection is not successful")