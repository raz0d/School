# QUESTION - 10

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

# ---------------------------------------
# LOGIC 2
