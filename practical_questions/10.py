import pickle as p
def create_file():
    f = open("create_file.dat", "wb")
    content = [
        [1, "anuj", 33],
        [2, "Aditya", 34],
        [3, "ansh", 12],
        [4, "alsamad", 43]
    ]
    for i in content:
        p.dump(i, f)
    f.close()

def update_records():
    f = open("create_file.dat", "rb")
    updated_cnt = []
    rno = int(input("enter roll no: "))
    found = False
    while True:
        try:
            cnt = p.load(f)
            if cnt[0] == rno:
                new_marks = int(input("enter marks: "))
                cnt[2] = new_marks
                updated_cnt.append(cnt)
                found = True
            else:
                updated_cnt.append(cnt)
        except:
            if not found:
                print("rno not found")
            break
    f.close()

    f = open("create_file.dat", "wb")
    for i in updated_cnt:
        p.dump(i, f)
    f.close()

def read():
    f = open("create_file.dat", "rb")
    while True:
        try:
            cnt = p.load(f)
            print(cnt)
        except:
            break

create_file()
update_records()
read()