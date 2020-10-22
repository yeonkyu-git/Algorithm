import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
res = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    getMoney = 0
    if a == b and b == c:
        getMoney = 10000 + a * 1000
    elif a == b:
        getMoney = 1000 + a * 100
    elif b == c:
        getMoney = 1000 + b * 100
    elif a == c:
        getMoney = 1000 + a * 100
    else:
        getMoney = max(a, b, c) * 100

    if res < getMoney:
        res = getMoney

print(res)