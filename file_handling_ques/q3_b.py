def RevString():
    with open("Input.txt") as file:
        lines = file.readlines()
        for line in lines:
            str = ""
            for word in line.split():
                if word[0].lower() == "o":
                    str += word[::-1]
                    str += " "
                else:
                    str += word
                    str += " "
            print(str)


RevString()