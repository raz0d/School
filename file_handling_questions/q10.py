import csv

def Accept():
    with open("Result.csv", "w", newline="") as f:
        fwrite = csv.writer(f)
        res = "y"
        K = ["Student ID", "Student Name", "Game Name", "Result"]
        fwrite.writerow(K)
        while res == "y":
            St_Id = int(input("Student ID: "))
            ST_name = input("Student name: ")
            Game_Name = input("Game game: ")
            Result = input("Enter result: ")
            if Result not in "WonLostTie":
                print("Enter a valid result")
                break
            L = [St_Id, ST_name, Game_Name, Result]
            fwrite.writerow(L)
            res = input("Add more record: ")
        print("Records added successfully")

def wonCount():
    with open("Result.csv", "r") as f:
        fread = csv.reader(f)
        w = 0
        for i in fread:
            if i[3] == "Won":
                w += 1
        print(f"{w} students have won the game")

Accept()
wonCount()