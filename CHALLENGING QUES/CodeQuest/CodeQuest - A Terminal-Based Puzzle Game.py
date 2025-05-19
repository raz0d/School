import random

lives = 3
score = 0
def main():
    print("Welcome to CodeQuest - Python Puzzle Adventure!\n")

    print('''
        1. Start New Game
        2. Load Game
        3. Exit\n
    ''')
    try:
        choice = int(input("Enter your chice: \n"))
    except:
        print("Enter an integer or RageQuit")
    return choice

def level3():
    return

def level2():
    global score
    global lives

    print("Level 2: The Pattern Unlocker")

    patterns = [[2, 4, 8, 16, 32], [2, 3, 5, 7, 11], [1, 2, 6, 24], [10, 20, 15, 25, 20], [2, 3, 5, 8, 13]]
    pattern = random.choice(patterns)

    answers = [64, 17, 120, 30, 21]

    print("Puzzle: Find the next number of the sequence - ")
    for i in pattern:
        print(i, end="")
    print()

    answer = input("Your Answer: ")

    serial = patterns.index(pattern)

    if answer == answers[serial]:
        print("✅ Correct! +10 points", "\n")
        score += 10
    else:
        print("❎ Wrong! -10 points", "\n")
        score -= 10
        lives -= 1

    if lives == 0:
        return "Game Over 🚫🚫🚫"
    else:
        print(f"Lives left: {lives} | Score: {score} \n")

    choice = input("Do you want to continue to Level 2? (yes/no): ")

    if choice.lower() == "no":
        return f"🙅‍♂️ Game End: Score: {score}"
    else:
        level3()

def level1():
    global score
    global lives

    print("Level 1: The Reverser")

    words = ["PYTHON", "LEVEL", "COMPUTER", "PROGRAM", "STRING", "VARIABLE"]
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
        return "Game Over 🚫🚫🚫"
    else:
        print(f"Lives left: {lives} | Score: {score} \n")

    choice = input("Do you want to continue to Level 2? (yes/no): ")

    if choice.lower() == "no":
        return f"🙅‍♂️ Game End: Score: {score}"
    else:
        level2()