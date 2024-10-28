import csv

def Add_Device():

    with open("peripheral.csv", "w", newline="") as f:
        fwrite = csv.writer(f)
        res = "y"

        while res == "y":
            P_id = input("Device ID: ")
            P_name = input("Device name: ")
            Price = input("Device price: ")
            l = [P_id, P_name, Price]
            fwrite.writerow(l)
            res = input("Add more records ? (y/n): ")

        print("Records added successfully")

def Count_Device():
    c = 0

    with open("peripheral.csv", "r") as f:
        fread = csv.reader(f)
        for i in fread:
            if int(i[2]) < 1000:
                print(i)
                c += 1
        print("No of devices with price less than 1k: ", c)


Add_Device()
Count_Device()
