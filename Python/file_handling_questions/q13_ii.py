import csv

def add():
    with open("furdata.csv", "w", newline="") as f:
        fwr = csv.writer(f)
        res = "y"
        while res == "y":
            fid = input("Furniture ID: ")
            fname = input("Furniture name: ")
            fprice = input("Furniture price: ")
            fwr.writerow([fid, fname, fprice])
            res = input("Add more records? (y/n): ")
        print("Records added successfully")

def search():
    with open("furdata.csv", "r") as f:
        fread = csv.reader(f)
        for i in fread:
            if int(i[2]) > 10000:
                print(i)

add()
search()