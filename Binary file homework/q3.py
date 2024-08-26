import pickle as p

def search_Balaghat():
    with open("travels.dat", "rb") as f:
        found = False
        while True:
            try:
                cnt = p.load(f)
                if cnt[2] == "Balaghat":
                    print(cnt)
                    found = True
            except:
                if not found:
                    print("No record found")
                break

search_Balaghat()