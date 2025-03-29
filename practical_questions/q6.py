f1 = open("myfile.txt")
f2 = open("to_write.txt", "a")
cnt1 = f1.readlines()
for i in cnt1:
    if "a" in i:
        f2.writelines([i])
f1.close()
f2.close()
