import pickle as p

file = open("test1.dat", "wb")
cnt1 = [["alsamad", 2], ["anuj", 3], ["aditya", 6], ["ansh", 5]]
for i in cnt1:
    p.dump(i, file)
file.close()

file = open("test1.dat", "rb")
rno = int(input("roll no: "))
found = False
while True:
    try:
        cnt = p.load(file)
        if cnt[1] == rno:
            print(cnt[0])
            found = True
    except:
        if not found:
            print("not found")
        break
file.close()
