def LongLines():
    with open("lines.txt") as file:
        for i in file.readlines():
            if len(i.split()) >= 10 :
                print(i, end="")
LongLines()