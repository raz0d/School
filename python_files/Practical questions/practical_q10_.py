# QUESTION - 10
# SIMPLE AND EASY LOGIC


import pickle as p

def create_file():
    with open("myfile1.dat", "wb") as f:
        ans = "y"
        while ans == "y":
            rno = int(input("Enter roll no: "))
            name = input("Enter name: ")
            marks = int(input("enter marks: "))
            p.dump([rno, name, marks], f)
            ans = input("add more records? : ")
    print("Records added successfully")

def update_marks():
    n = int(input("enter roll no: "))
    found = False
    with open("myfile1.dat", "rb+") as f:
        while True:
            try:
                loc = f.tell()
                cnt = p.load(f)
                if cnt[0] == n:
                    f.seek(loc)
                    m = int(input("new marks: "))
                    cnt[2] = m
                    p.dump(cnt, f)
                    found = True
                    break
            except:
                if found:
                    print("Mark changes successfully")
                else:
                    print("No record with this roll no")
                break


create_file()
update_marks()

with open("myfile1.dat", "rb") as f:
    print("\n\nREADING")
    while True:
        try:
            cnt = p.load(f)
            print(cnt)
        except:
            break


# ---------------------------------------
# LOGIC 2

# import pickle as p
#
# creating_file = open("test_file.dat", "wb")
#
# def add_records():
#     response = "y"
#     record_list = []
#     while response.lower() == "y":
#         name = input("Enter name: ")
#         roll_no = int(input("Enter roll number: "))
#         marks = int(input("Enter marks: "))
#         record_list.append({"name": name, "roll_no": roll_no, "marks": marks})
#         response = input("Add more record ? (y/n): ")
#     return record_list
#
# for record in add_records():
#     p.dump(record, creating_file)
#
# creating_file.close()
#
# print("\nChange marks:")
# file = open("test_file.dat", "rb")
#
# def change_marks():
#     updated_content = []
#     rn = int(input("Enter roll number: "))
#     found = False
#     while True:
#         try:
#             content =  p.load(file)
#             if content["roll_no"] == rn:
#                 nm = int(input("Enter new marks: "))
#                 content["marks"] = nm
#                 updated_content.append(content)
#                 found = True
#             else:
#                 updated_content.append(content)
#         except:
#             break
#     if not found:
#         print("No student with this roll number")
#     rerun = input("Change marks again ? (y/n) : ")
#     if rerun == "y":
#         file.seek(0)
#         change_marks()
#     return updated_content
#
# updated_content = change_marks()
# file.close()
#
# open("test_file.dat", "wb").close()
#
# with open("test_file.dat", "wb") as final_file:
#     for record in updated_content:
#         p.dump(record, final_file)

