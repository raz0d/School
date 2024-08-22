import pickle as p

def copyData():
    with open("sport.dat", "rb") as file:
        list = []
        while True:
            try:
                cnt = p.load(file)
                if cnt[0] == "BasketBall":
                    list.append(cnt)
            except:
                break

    with open("basket.dat", "wb") as file:
        for i in range(len(list)):
            p.dump(list[i], file)

    return len(list)