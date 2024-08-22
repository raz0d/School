# QUESTION 12

import csv

def search_record():
    with open("myfile.csv", "r") as f:
        readobj = csv.reader(f)
        for i in readobj:
            rate = float(i[2])
            if 500 < rate < 1000:
                print(i)