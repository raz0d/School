import pickle as p

def Add_Device():
    with open("peripheral.csv", "wb") as file:
        r = "y"
        while r == "y":
            P_id = input("Device id: ")
            P_name = input("Device name: ")
            Price = input("Device price : ")
            r = [P_id, P_name, Price]
            p.dump(r, file)
            r = input("enter more records? (y/n): ")
        print("Records added successfully")


