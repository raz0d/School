import pickle as p

def HighPaid():
    with open("Employee.dat", "rb") as f:
        c = 0
        found = False
        while True:
            try:
                cnt = p.load(f)
                if cnt["EmpSalery"] >= 25000:
                    c += 1
                    found = True
                    print(cnt)
            except:
                if not found:
                    print("No record found")
                else:
                    print("No of employees: ", c)
                break

HighPaid()