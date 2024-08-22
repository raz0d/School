def y_book():
    with open("Bookname.txt") as file:
        for line in file.readlines():
            if "y" in line.lower():
                print(line, end="")
y_book()