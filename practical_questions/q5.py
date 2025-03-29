file = open("myfile.txt")
cnt = file.read()
v = 0
c = 0
u = 0
l = 0
for i in cnt:
    if i in "aeiouAEIOU":
        v += 1
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
    elif i not in "aeiouAEIOU" and i.isalpha():
        c += 1
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
print("vowel", v)
print("consonant", c)
print("uppr", u)
print("lower", l)