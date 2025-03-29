import csv
file = open("data.csv", "r")
reader_obj = csv.reader(file)
for i in reader_obj:
    if (int(i[2])>=500) and (int(i[2])<=1000):
        print(i)
file.close()

