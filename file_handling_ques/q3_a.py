def y_book():
    with open("Bookname.txt") as file:
        lines = file.readlines()
        for line in lines:
            if "y" in line.lower():
                print(line, end="")
y_book()