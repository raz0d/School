# QUESTION 13

import csv

def create_csv_file():
    with open("myfile.csv", "w", newline="") as f:
        writeobj = csv.writer(f)
        res = "y"
        while res == "y":
            user_id = input("Enter user id: ")
            pass_ = input("Enter password: ")
            writeobj.writerow([user_id, pass_])
            res = input("Add more record? (y/n): ")

def search_record():
    uid = input("enter user id: ")
    with open("myfile.csv", "r") as f:
        readobj = csv.reader(f)
        found = False
        for i in readobj:
            if i[0] == uid:
                print("Pass is: ", i[1])
                found = True
        if not found:
            print("No record found")

create_csv_file()
search_record()