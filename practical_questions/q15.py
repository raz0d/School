def linear_search(stack, element):
    loc = None
    found = False
    for i in range(len(stack)):
        if element == stack[i]:
            loc = i
            found = True
            return loc
    else:
        if not found:
            return -1
stack = [1,2,3,4,5]
element = 3
print(linear_search(stack, element))