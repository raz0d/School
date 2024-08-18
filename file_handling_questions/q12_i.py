def COUNTLINES():
    with open("testfile.txt") as file:
        lines = 0
        for i in file.readlines():
            if i[0] not in "aeiouAEIOU":
                lines += 1
        print("The number of lines not staring with any vowel: ", lines)
COUNTLINES()