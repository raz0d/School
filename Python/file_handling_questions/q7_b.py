import csv

def Add_Book():
    with open("Book.csv", "w", newline="") as f:
        fwrite = csv.writer(f)
        res = "y"
        while res == "y":
            book_ID = input("Book ID: ")
            B_name = input("Book name: ")
            pub = input("Publisher: ")
            l = [book_ID, B_name, pub]
            fwrite.writerow(l)
            res = input("Add more records? ")
        print("Records added successfully")

def Search_Book():

    with open("Book.csv", "r") as f:
        fread = csv.reader(f)
        p = input("Enter publisher name: ")
        found = False
        c = 0

        for i in fread:
            if i[2] == p:
                print(i)
                c += 1
                found = True
        if not found:
            print("No book found")
        print("No of book published: ", c)

Add_Book()
Search_Book()