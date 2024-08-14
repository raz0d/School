# QUESTION 7

created_file = open("created_file.txt", "w")
content = ["This is first line\n", "python is fun\n", "my name is razod\n", "and my roll number is 007\n"]
created_file.writelines(content)
created_file.close()

file = open("created_file.txt")
def lines_with_T_P():
    file_content = file.readlines()
    for line in file_content:
        if line[0] in "TPtp":
            print(line, end="")

lines_with_T_P()

file.close()