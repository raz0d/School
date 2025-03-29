file = open("myfile.txt")
cnt = file.read()
he = 0
she = 0
for i in cnt.split():
    if i in ["he", "He"]:
        he += 1
    elif i in ["she", "She"]:
        she += 1
print("He: ", he)
print("She: ", she)