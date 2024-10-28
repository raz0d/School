import csv

def COURIER_ADD():
    with open("courier.csv", "w", newline="") as f:
        fwrite = csv.writer(f)
        res = "y"
        while res == "y":
            cid = input("Courier ID: ")
            s_name = input("Sender name: ")
            source = input("Source: ")
            destination = input("Address: ")
            l = [cid, s_name, source, destination]
            fwrite.writerow(l)
            res = input("Add more record ? (y/n): ")
        print("Records added successfully !")

def COURIER_SEARCH():
    des = input("enter designation: ")
    with open("courier.csv", "r") as f:
        fread = csv.reader(f)
        found = False
        for i in fread:
            if i[3] == des:
                print(i)
                found = True
        if not found:
            print("No records found")

COURIER_ADD()
COURIER_SEARCH()
