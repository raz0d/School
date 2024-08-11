file = open(r"C:\Users\alsam\Desktop\School\text_files\myfile.txt")
content = file.read()

def count_he_she():
    he = 0
    she = 0
    words = content.split()
    for word in words:
        word = word.lower()
        if word == "he":
            he += 1
        elif word == "she":
            she += 1
    return he, she

he, she = count_he_she()
print(f"Frequency of he is {he} and frequency of she is {she}")

file.close()