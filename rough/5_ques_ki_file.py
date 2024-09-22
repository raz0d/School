# QUESTION - 1
file = open("Article.txt")
cnt = file.readlines()
ll = ""
for i in cnt:
    if len(i)> len(ll):
        ll = i
print(i)