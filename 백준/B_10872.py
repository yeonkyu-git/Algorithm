

def factorial(n):
    total = 1
    while n > 0:
        total *= n
        n -= 1

    return total


n = int(input())
print(factorial(n))
