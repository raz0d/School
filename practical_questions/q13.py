import csv

def add_records():
    file = open("data1.csv", "w", newline="")
    writer_obj = csv.writer(file)
    ans = "y"
    while ans == "y":
        id = input("Enter user ID: ")
        pass_ = int(input("Enter password: "))
        cnt = [id, pass_]
        writer_obj.writerow(cnt)
        ans = input("add more records? (y/n): ")
    file.close()

def search_records():
    file = open("data1.csv", "r")
    reader_obj = csv.reader(file)
    user_id = input("enter user id: ")
    for i in reader_obj:
        if i[0] == user_id:
            print("pass: ", i[1])
    file.close()

add_records()
search_records()