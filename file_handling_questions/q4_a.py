import csv

def Add_Teacher():

    with open("Teacher.csv", "w", newline="") as f:
        fwrite = csv.writer(f)
        res = "y"

        while res == "y":
            T_id = int(input("Teacher ID: "))
            Tname = input("Teacher name: ")
            desig = input("Enter designation: ")
            fwrite.writerow([T_id, Tname, desig])
            res = input("Add more records? (y/n): ")
        print("Records added successfully !")

def Search_Teacher():

    with open("Teacher.csv", "r") as f:
        fread = csv.reader(f)
        print("ALL PGT TEACHERS")

        for i in fread:
            if i[2] == "PGT":
                print(i)

Add_Teacher()
Search_Teacher()