# QUESTION - 9

import pickle as p

creating_file = open("test_file.dat", "wb")

response = "y"
record_list = []

while response.lower() == "y":
    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    record_list.append({"name": name, "roll_no": roll_no})
    response = input("Add more record ? (y/n): ")

for record in record_list:
    p.dump(record, creating_file)

creating_file.close()

file = open("test_file.dat", "rb")

print("\nFind name using roll number")

def search_name():

    srn = int(input("Enter roll number: "))
    found = False

    while True:
        try:
            file_content = p.load(file)
            if file_content["roll_no"] == srn:
                print(file_content["name"])
                found = True
        except:
            break
    if not found:
        print("No name found of this roll number")

    file.seek(0)

    rerun = input("want to find another name ? (y/n): ")
    if rerun == "y":
        search_name()

search_name()
file.close()