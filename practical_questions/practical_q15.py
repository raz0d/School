# QUESTION 15

stack = [10, 23, 45, 70, 11, 15]

def linear_search(stack, value):
    for i in range(len(stack)):
        if stack[i] == value:
            return i
    return -1 # -1 if value not found

value = int(input("Number to search: "))

loc = linear_search(stack, value)

if loc != -1:
    loc_from_top = len(stack) - 1
    print(f"Element found at position {loc_from_top} from the top")
else:
    print("Element not found")
