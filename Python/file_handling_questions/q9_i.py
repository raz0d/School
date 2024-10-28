def You_lines():
    with open("Alpha.txt") as file:
        for l in file.readlines():
            if l.startswith("You"):
                print(l, end="")
You_lines()