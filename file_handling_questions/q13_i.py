import csv

def ADD():
    with open("record.csv", "w", newline="") as f:
        fwr = csv.writer(f)
        res = "y"
        while res == "y":
            empid = input("Employee ID: ")
            name = input("Employee name: ")
            mobile = input("Employee salary: ")
            l = [empid, name, mobile]
            fwr.writerow(l)
            res = input("Add record? (y/n): ")
        print("Records added successfully")

def COUNTER():
    with open("record.csv", "r") as f:
        fread = csv.reader(f)
        cnt = list(fread)
        print("No of records: ", len(cnt))

ADD()
COUNTER()