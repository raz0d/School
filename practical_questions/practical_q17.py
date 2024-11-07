# QUESTION 17

def pdb7(stack, num):
    for i in num:
        if i % 7 == 0:
            stack.append(i)
    print("Elements divisible by 7 pushed to stack")

def show(stack):
    if not stack:
        print("Stack is empty")
    else:
        print("Stack contents:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

stack = []
num = [14, 28, 35, 40, 49, 50, 63, 77]

pdb7(stack, num)
show(stack)
