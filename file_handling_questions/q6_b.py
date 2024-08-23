def count_Dwords():
    with open("details.txt") as f:
        c = 0
        for i in f.read().split():
            if i[-1].isdigit():
                c += 1
        print("Number of words ending with a digit are", c)

count_Dwords()