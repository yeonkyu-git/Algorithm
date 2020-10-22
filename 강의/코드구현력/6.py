import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))

def digit_sum(x):
    total = 0
    while x != 0:
        total += x % 10
        x //= 10
    return total

def digit_sum2(x):
    sumNumber = 0
    for i in str(x):
        sumNumber += int(i)
    print(sumNumber)
    return sumNumber

digit_sum2(125)



maxNumber = 0
answer = 0
for val in s:
    tot = digit_sum(val)
    if maxNumber < tot:
        maxNumber = tot
        answer = val

print(val)