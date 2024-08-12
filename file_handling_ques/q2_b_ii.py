import pickle as p

with open("emp.dat", "wb+") as file:
    cnt = [[154, "Alsamad", 45000], [546, "Aditya", 15000], [324, "Ansh", 24000]]
    for i in range(len(cnt)):
        p.dump(cnt[i], file)
    file.seek(0)
    while True:
        try:
            content = p.load(file)
            print(content)
        except:
            break


def disp_detail():
    with open("emp.dat", "rb") as file:
        while True:
            try:
                content = p.load(file)
                if content[2] < 25000:
                    print("Employee number: ", content[0])
                    print("Employee name: ", content[1])
            except:
                break

disp_detail()