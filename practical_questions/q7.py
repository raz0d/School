file = open("text_file_created.txt", "w")
cnt1 = ["hell this is line one poppop \n", "line 2 ye hai Terret\n", "line 3 yo hai Tehhe Pdf tg"]
file.writelines(cnt1)
file.close()

file = open("text_file_created.txt", "r")
cnt2 = file.read()
t = 0
p = 0
for i in cnt2.split():
    if i[0] in "tT":
        t += 1
    elif i[0] in "pP":
        p += 1
print("p: ", p)
print("t: ", t)