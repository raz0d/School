file = open("myfile.txt")
line = file.readline()
while line:
    k = line.split()
    for i in k:
        print(i, end="#")
    line = file.readline()