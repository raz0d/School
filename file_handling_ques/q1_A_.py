with open("story.txt", "w") as f:
    f.write("Our parents told us that we must eat vegetables to be healthy. And it turns out, our parents were right! So, what else did our parents tell?")

def showInLines():

    with open("story.txt") as file:
        content = file.read()

    sentences_list = []
    sentence = ""

    for i in content:
        sentence += i
        if i in ['.', '?', '!']:
            sentences_list.append(sentence)
            sentence = ""
    for sentence in sentences_list:
        print(sentence)

showInLines()