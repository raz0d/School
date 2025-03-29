import random
l = []
for i in range(1, 11):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    summ = r1 + r2
    print(f"round number {i}: sum = {summ}")
    l.append(summ)
k = 0
for i in l:
    k += i
print("total: ", k)
