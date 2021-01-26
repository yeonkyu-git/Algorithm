import sys
from collections import deque
sys.stdin = open('imput.txt', 'rt')

a, b = map(int, input().split())
dq = deque(i+1 for i in range(a))

while len(dq) != 1:
    for _ in range(b-1):
        number = dq.popleft()
        dq.append(number)
    dq.popleft()

print(dq[0])

