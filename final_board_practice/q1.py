def check_prime(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n >1:
        for i in range(2, n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return "Enter a number greater than 0"

for i in range(1, 101):
    if check_prime(i):
        print(i)