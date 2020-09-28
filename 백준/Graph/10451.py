from collections import deque
import sys

def bfs(v):
    start = v
    visit[v] = 1
    q = deque()
    q.append(v)
    while(q):
        b = q.popleft()   # Index
        if visit[s[b]] == 0:
            visit[s[b]] = 1
            q.append(s[b])

    return 1




a = int(sys.stdin.readline())
for i in range(a):
    n = int(sys.stdin.readline())
    s = [0]
    s = s + list(map(int, sys.stdin.readline().strip().split()))
    visit = [0 for i in range(n + 1)]

    count = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            count += bfs(i)

    print(count)