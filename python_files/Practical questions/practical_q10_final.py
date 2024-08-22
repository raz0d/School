import pickle as p

def create_file():
    with open("myfile1.dat", "wb") as f:
        ans = "y"
        while ans == "y":
            rno = int(input("Enter roll no: "))
            name = input("Enter name: ")
            marks = int(input("enter marks: "))
            p.dump([rno, name, marks], f)
            ans = input("add more records? : ")
    print("Records added successfully")

def update_marks():
    n = int(input("Enter roll no: "))
    l = []
    found = False
    with open("myfile1.dat", "rb") as f:
        while True:
            try:
                cnt = p.load(f)
                if cnt[0] == n:
                    m = int(input("Enter new marks: "))
                    cnt[2] = m
                    found = True
                l.append(cnt)
            except:
                if not found:
                    print("No record found")
                else:
                    print("Marks updated")
                break

    with open("myfile1.dat", "wb") as f:
        for i in l:
            p.dump(i, f)

create_file()
update_marks()