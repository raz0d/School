import pickle as p

data = [
    {"name": "Alsamad", "roll_no": 7, "marks": 56},
    {"name": "Anuj", "roll_no": 12, "marks": 65},
    {"name": "Ansh", "roll_no": 11, "marks": 78}
]

with open("test_file.dat", "wb") as f:
    for i in data:
        p.dump(i, f)

f = open("test_file.dat", "rb+")
found = False
rno = int(input("Enter roll number: "))
while True:
    try:
        p_locatn = f.tell()
        cnt = p.load(f)
        if cnt["roll_no"] == rno:
            new_m = int(input("Enter new marks: "))
            cnt["marks"] = new_m
            f.seek(p_locatn)
            p.dump(cnt, f)
            found = True
    except:
        break
if found:
    print("Data updated successfully")
else:
    print("No data found with this roll number")

f.seek(0)
while True:
    try:
        k = p.load(f)
        print(k)
    except:
        break
        
f.close()