def longest_line():
    with open("Article.txt") as f:
        cnt = f.readlines()
        temp = 0
        for i in cnt:
            if len(i) > temp:
                ll = i
                temp = len(i)
        print("Longest line: ", ll)
longest_line()