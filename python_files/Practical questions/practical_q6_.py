#QUESTION - 6

read_file = open(r"C:\Users\alsam\Desktop\School\text_files\myfile.txt", "r")
content_list = read_file.readlines()
read_file.close()

def no_a_lines():
    new_list = []
    for line in content_list:
        if "a" not in line:
            new_list.append(line)
    return new_list

def a_lines():
    new_list = []
    for line in content_list:
        if "a" in line:
            new_list.append(line)
    return new_list

open(r"C:\Users\alsam\Desktop\School\text_files\myfile.txt", "w").close()

with open(r"C:\Users\alsam\Desktop\School\text_files\myfile.txt", "w") as file:
    file.writelines(no_a_lines())

write_file = open(r"C:\Users\alsam\Desktop\School\text_files\to_write.txt", "w")
for i in range(len(a_lines())):
    write_file.write(a_lines()[i])

write_file.close()
