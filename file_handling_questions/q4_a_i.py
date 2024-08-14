import pickle as p

def add_record():
    with open("Teacher.csv", "wb") as file:
        r = "y"
        while r == "y":
            T_id = input("teacher id: ")
            tname = input("teacher name: ")
            desig = input("teacher designation: ")
            r = [T_id, tname, desig]
            p.dump(r, file)
            r = input("enter more records? (y/n): ")
        print("Records added successfully")

add_record()
