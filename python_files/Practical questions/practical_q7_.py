# QUESTION 7

def lines_with_T_P():
    with open("created_file.txt") as file:
        file_content = file.readlines()
        for line in file_content:
            if line[0] in "TPtp":
                print(line, end="")

lines_with_T_P()
