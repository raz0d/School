# QUESTION - 3

def min_max_avg(l):
    if len(l) == 0:
        return None, None, None

    min = l[0]
    max = l[0]
    sum = 0

    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    avg = sum / len(l)

    return min, max, avg

# TESTING THE FUNCTION

marks = eval(input("Enter list of marks: "))
min_mark, max_mark, avg_mark = min_max_avg(marks)

print("Minimum mark: ", min_mark)
print("Maximum mark: ", max_mark)
print("Average mark: ", avg_mark)