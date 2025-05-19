import random

lives = 3
score = 0
def main():
    print("Welcome to CodeQuest - Python Puzzle Adventure!\n")

    print('''
        1. Start New Game
        2. Load Game
        3. Exit
    ''')
    try:
        choice = int(input("Enter your chice: "))
    except:
        print("Enter an integer or RageQuit")
    return choice
def level4():
    global score
    global lives

def level3():
    global score
    global lives

    print("\n")
    print("Level 3: Palindrome Gate")

    words = [
        "LEVEL", "RADAR", "CIVIC", "DEED", "NOON",
        "ROTOR", "MADAM", "REFER", "MALAYALAM", "RACECAR",
        "PYTHON", "HELLO", "WORLD", "PROGRAM", "LOOP",
        "STRING", "RANDOM", "COMPUTER", "DEVELOPER", "GITHUB"
    ]
    word = random.choice(words)
    serial = words.index(word)

    print("Task: Check if the word is a palindrome- ", word)

    answer = input("Yes or No: ")

    if serial<10 and answer.lower() == "yes":
        print("✅ Correct! +10 points", "\n")
        score += 10
    else:
        print("❎ Wrong! -10 points", "\n")
        score -= 10
        lives -= 1

    if lives == 0:
        print("Game Over 🚫🚫🚫")
        return
    else:
        print(f"Lives left: {lives} | Score: {score} \n")

    choice = input("Do you want to continue to Level 4? (yes/no): ")

    if choice.lower() == "no":
        try:
            print("What do you want ?\n1. Repeat\n2. Previous Level\n3. Exit")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                level3()
            elif choice2 == 2:
                level2()
            else:
                print("🙅‍♂️ Game End: Score: {score}")
                return
        except:
            print("Enter an integer dumbass 🤦 ")
            return
    else:
        level4()

def level2():
    global score
    global lives

    print("\n")
    print("Level 2: The Pattern Unlocker")

    patterns = [
        [2, 4, 8, 16, 32], [2, 3, 5, 7, 11], [1, 2, 6, 24], [10, 20, 15, 25, 20], [2, 3, 5, 8, 13]
    ]
    pattern = random.choice(patterns)
    serial = patterns.index(pattern)

    answers = [64, 13, 120, 30, 21]

    print("Puzzle: Find the next number of the sequence - ")
    for i in pattern:
        print(i, end=" ")
    print()

    answer = int(input("Your Answer: "))

    if answer == answers[serial]:
        print("✅ Correct! +10 points", "\n")
        score += 10
    else:
        print("❎ Wrong! -10 points", "\n")
        score -= 10
        lives -= 1

    if lives == 0:
        print("Game Over 🚫🚫🚫")
        return
    else:
        print(f"Lives left: {lives} | Score: {score} \n")

    choice = input("Do you want to continue to Level 3? (yes/no): ")

    if choice.lower() == "no":
        try:
            print("What do you want ?\n1. Repeat\n2. Previous Level\n3. Exit")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                level2()
            elif choice2 == 2:
                level1()
            else:
                print("🙅‍♂️ Game End: Score: {score}")
                return
        except:
            print("Enter an integer dumbass 🤦 ")
            return
    else:
        level3()

def level1():
    global score
    global lives

    print("\n")
    print("Level 1: The Reverser")

    words = [
        "PYTHON", "LEVEL", "COMPUTER", "PROGRAM", "STRING", "VARIABLE"
    ]
    word = random.choice(words)
    print("Puzzle: Reverse this Word: ", word, "\n")

    answer = input("Your answer: ")

    if answer.lower() == word[::-1].lower():
        print("✅ Correct! +10 points", "\n")
        score += 10
    else:
        print("❎ Wrong! -10 points", "\n")
        score -= 10
        lives -= 1

    if lives == 0:
        print("Game Over 🚫🚫🚫")
        return
    else:
        print(f"Lives left: {lives} | Score: {score} \n")

    choice = input("Do you want to continue to Level 2? (yes/no): ")

    if choice.lower() == "no":
        try:
            print("What do you want ?\n1. Repeat\n2. Exit")
            choice2 = int(input("Your choice?: "))
            if choice2 == 1:
                level1()
            else:
                print("🙅‍♂️ Game End: Score: {score}")
                return
        except:
            print("Enter an integer dumbass 🤦 ")
            return
    else:
        level2()

main()
level1()