# QUESTION - 4

file = open("myfile.txt")
def words_with_sep():
    line = file.readline()
    while line:
        list = line.split()
        new_line = "#".join(list)
        print(new_line)
        line = file.readline()
words_with_sep()

file.close()