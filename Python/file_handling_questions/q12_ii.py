def ETCount():
    with open("testfile2.txt") as file:
        e = 0
        t = 0
        for i in file.read():
            if i in "eE":
                e += 1
            elif i in "tT":
                t += 1
        print("E or e: ", e)
        print("T or t: ", t)
ETCount()