import pickle as p
def findAType(mtype):
    with open("CINEMA.dat", "rb") as f:
        found = False
        while True:
            try:
                cnt = p.load(f)
                for i in cnt.values():
                    if i[1] == mtype:
                        print(i)
                        found = True
            except:
                if not found:
                    print("No record found")
                break


findAType(input("enter movie type: "))