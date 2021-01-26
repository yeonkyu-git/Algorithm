import sys
from collections import deque
sys.stdin = open('imput.txt', 'rt')

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):   # any : 하나라도 나오면 false 임
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
