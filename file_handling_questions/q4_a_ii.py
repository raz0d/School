import pickle as p

def PGT_teachers():
    with open("Teacher.csv", "rb") as f:
        while True:
            try:
                r = p.load(f)
                if r[2] == "PGT":
                    print(r)
            except:
                break

PGT_teachers()