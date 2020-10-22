import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))

def digit_sum(x):
    total = 0
    while x != 0:
        total += x % 10
        x //= 10
    return total

maxNumber = 0
idx = 0
for i in range(n):
    temp = digit_sum(s[i])
    if maxNumber < temp:
        maxNumber = temp
        idx = i

print(s[idx])