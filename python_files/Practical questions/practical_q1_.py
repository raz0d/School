# QUESTION  - 1

def calculator():
    a = float(input("Enter first number: "))
    sign = input("Enter operation (+, -, *, /) : ")
    b = float(input("Enter second number: "))

    if sign == "+":
        print(f"{a} + {b} = {a+b}")
    elif sign == "-":
        print(f"{a} - {b} = {a-b}")
    elif sign == "*":
        print(f"{a} * {b} = {a*b}")
    elif sign == "/":
        if b>0 or b<0:
            print(f"{a} / {b} = {a/b}")
        else:
            print("ZeroDivisionError")

    decision = input("\nWant to calculate again? (y/n): ")
    if decision == "y":
        calculator()

calculator()