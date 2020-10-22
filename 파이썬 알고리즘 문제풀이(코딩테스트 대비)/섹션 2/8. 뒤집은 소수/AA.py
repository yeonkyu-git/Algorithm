import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))

def reverse(x):
    reversNumber = ""
    for i in str(x):
        reversNumber = i + reversNumber

    return int(reversNumber)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

for val in s:
    rNumber = reverse(val)
    if isPrime(rNumber):
        print(rNumber, end=' ')