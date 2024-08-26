# QUESTION - 5

file = open("myfile.txt")

def file_analysis():
    file_content = file.read()

    vowels = 0
    consonents = 0
    uppercase = 0
    lowercase = 0

    for i in file_content:
        if i in "aeiouAEIOU":
            vowels += 1
            if i.islower():
                lowercase += 1
            else:
                uppercase += 1
        elif i.isalpha():
            consonents += 1
            if i.islower():
                lowercase += 1
            else:
                uppercase += 1

    print("Number of vowels: ", vowels)
    print("Number of consonents: ", consonents)
    print("Number of uppercase letters: ", uppercase)
    print("Number of lowecase letters: ", lowercase)

file_analysis()

file.close()