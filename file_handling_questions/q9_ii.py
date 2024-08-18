def vowelCount():
    with open("poem.txt") as file:
        v = 0
        for i in file.read():
            if i in "aeiouAEIOU":
                v += 1
        print("Number of vowels: ", v)

vowelCount()