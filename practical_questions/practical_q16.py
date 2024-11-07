# QUESTION - 16

def isEmpty(s):
    return len(s) == 0

def push(s, item):
    s.append(item)
    print(f"{item} pushed to stack")

def pop(s):
    if isEmpty(s):
        return "StackUnderFlow"
    else:
        return s.pop()

def peek(s):
    if isEmpty(s):
        return "StackUnderFlow"
    else:
        return s[-1]  

def show(s):
    if isEmpty(s):
        print("No element in stack")
    else:
        print("Stack contents:")
        for i in range(len(s) - 1, -1, -1):
            print(s[i])

# MAIN PROGRAM START

s = []

while True:
    print("\n=== Stack Operations ===")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Show stack")
    print("5. Exit")

    oc = int(input("Operation choice: "))

    if oc == 1:
        val = int(input("Item to push: "))
        push(s, val)

    elif oc == 2:
        val = pop(s)
        if val == "StackUnderFlow":
            print("Empty Stack")
        else:
            print("Deleted item:", val)

    elif oc == 3:
        val = peek(s)
        if val == "StackUnderFlow":
            print("Empty Stack")
        else:
            print("Top value:", val)

    elif oc == 4:
        show(s)

    elif oc == 5:
        print("Bye - Bye")
        break

    else:
        print("Invalid choice. Please select again.")
