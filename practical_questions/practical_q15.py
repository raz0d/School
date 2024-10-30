# Stack implementation using a list
stack = []

# Function to push elements into the stack
def push(element):
    stack.append(element)
    print(f"{element} pushed to stack")

# Function to perform linear search in the stack
def linear_search(stack, key):
    for index, element in enumerate(stack):
        if element == key:
            return f"Element {key} found at position {index + 1} in the stack."
    return f"Element {key} not found in the stack."

# Adding elements to the stack
push(10)
push(20)
push(30)
push(40)
push(50)

# Perform linear search
key = int(input("Enter the element to search in the stack: "))
result = linear_search(stack, key)
print(result)
