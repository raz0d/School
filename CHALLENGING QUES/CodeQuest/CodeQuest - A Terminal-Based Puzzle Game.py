
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

def level1():
    print("")