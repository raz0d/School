import pickle as p

with open("payment.dat", "rb") as f:
    found = False
    while True:
        try:
            cnt = p.load(f)
            if cnt[2] > 21000:
                print(cnt)
                found = True
        except:
            if not found:
                print("No record found")
            break
            
