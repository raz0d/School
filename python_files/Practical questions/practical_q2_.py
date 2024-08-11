# QUESTION - 2

def check_prime(n):

    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2, n):
            if n%i == 0:
                return False
        else:
            return True
    else:
        return "Enter a number greater than 1"

n = int(input("Enter a number to check: "))
print(check_prime(n))

print("All prime numbers from 1 to 100")
for i in range(1, 101):
    if check_prime(i):
        print(i)