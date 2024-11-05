import mysql.connector as sqLtor
con_obj = sqLtor.connect(host="localhost", user="root", passwd="0178", database="school")
print(con_obj)
if con_obj.is_connected():
    print("connection connected")
cursor_obj = con_obj.cursor()
query = '''
    SELECT itemname, type, price
    FROM furniture
    WHERE discount > 20
    ORDER BY dateofstock DESC;
    '''
cursor_obj.execute(query)
data = cursor_obj.fetchall()
for i in data:
    print(i)
con_obj.close()