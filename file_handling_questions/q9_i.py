def You_lines():
    with open("Alpha.txt") as file:
        s = file.readlines()
        for l in s:
            if l.startswith("You"):
                print(l, end="")
You_lines()