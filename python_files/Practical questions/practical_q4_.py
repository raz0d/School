# QUESTION - 4

file = open(r"C:\Users\alsam\Desktop\School\text_files\myfile.txt")
def words_with_sep():
    line = file.readline()
    while line:
        list = line.split()
        new_line = "#".join(list)
        print(new_line)
        line = file.readline()
words_with_sep()

file.close()