def vowelCount():
    with open("poem.txt") as file:
        s = file.read()
        v = 0
        for i in s:
            if i in "aeiouAEIOU":
                v += 1
        print("Number of vowels: ", v)

vowelCount()