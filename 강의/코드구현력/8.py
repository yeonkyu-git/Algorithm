import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))

def reverse(x):
    reversNumber = ""
    for i in str(x):
        reversNumber = i + reversNumber

    return int(reversNumber)

def reverse2(x):
    res = 0
    while x > 0:
        res = 10 * res + x % 10
        x //= 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False

    return True

for val in s:
    rNumber = reverse(val)
    if isPrime(rNumber):
        print(rNumber, end=' ')