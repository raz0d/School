import csv

file = open("myfile.csv", "r", newline="")
reader_obj = csv.reader(file)
for i in reader_obj:
    print(i)
file.close()
