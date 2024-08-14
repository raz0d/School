with open("words.txt", "w") as f:
    f.write("Our parents told us that we must eat vegetables to be healthy. And it turns out, our parents were right! So, what else did our parents tell?")

def c_words():
    file =  open("words.txt")
    cnt = file.read()
    upper = 0
    lower = 0
    for i in cnt:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
    print("Lower characters: ", lower)
    print("Upper characters: ", upper)

c_words()