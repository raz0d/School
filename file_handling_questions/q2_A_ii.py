import pickle as p

def addRecod():
    with open("items.dat", "wb+") as file:
        data = [
            {1: ["Alsamad", 700]},
            {2: ["Aditya", 1200]},
            {3: ["Ansh", 300]},
            {4: ["Anuj", 1300]},
            {5: ["Bhaibhav", 1500]}
        ]
        for i in data:
            p.dump(i, file)
        file.seek(0)
        while True:
            try:
                cnt = p.load(file)
                print(cnt)
            except:
                break

addRecod()

def Copy_new():
    f1 = open("items.dat", "rb")
    f2 = open("new_items.dat", "wb")

    while True:
        try:
            cnt = p.load(f1)
            for key, [name, amt] in cnt.items():
                if amt > 1000:
                    p.dump({key: [name, amt]}, f2)
        except:
            break
    f1.close()
    f2.close()

Copy_new()

with open("new_items.dat", "rb") as file:
    while True:
        try:
            cnt = p.load(file)
            print(cnt)
        except:
            break