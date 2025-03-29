def f(list):
    a = min(list)
    b = max(list)
    c = sum(list)/len(list)
    return a, b, c

list = eval(input("enter the list of marks: "))
min, max, avg = f(list)

print(min)
print(max)
print(avg)