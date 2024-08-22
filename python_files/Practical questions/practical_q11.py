# QUESTION 11

import csv

def read_csv():
    with open("myfile.csv", "r") as f:
        readobj = csv.reader(f)
        for i in readobj:
            print(i)