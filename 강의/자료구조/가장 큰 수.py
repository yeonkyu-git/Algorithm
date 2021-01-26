import sys
from collections import deque
sys.stdin = open('imput.txt', 'rt')
a, b = map(int, input().split())

a = list(map(int, str(a)))
originLen = len(a) - b
k = len(a) - b
answer = ''
while True:
    if b <= 0 or len(answer) == originLen:
        if len(answer) < originLen:
            for val in a:
                answer += str(val)
        break
    aLen = len(a)
    maxNumber = max(a[0:aLen - k + 1])

    for _ in range(0, aLen - k + 1):
        if a[0] == maxNumber:
            a.pop(0)
            break
        else:
            a.pop(0)
            b -= 1
    answer += str(maxNumber)
    k -= 1

print(answer)

