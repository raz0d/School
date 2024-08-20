# QUESTION - 8

def count_he_she():
    with open("myfile.txt") as file:
        content = file.read()
        he = 0
        she = 0
        for word in content.split():
            word = word.lower()
            if word == "he":
                he += 1
            elif word == "she":
                she += 1
    return he, she

he, she = count_he_she()
print(f"Frequency of he is {he} and frequency of she is {she}")
