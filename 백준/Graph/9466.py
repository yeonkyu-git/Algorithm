from collections import deque
import sys


def bfs(v):
    visit[v] = 1
    q = deque()
    q.append(v)
    temp_s = [v]
    while q:
        v = q.popleft()
        a = s[v]
        if visit[a] == 0:
            visit[a] = 1
            temp_s.append(a)
            q.append(a)
        else:
            if a in temp_s:
                return len(temp_s[temp_s.index(a):])

    return 0


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    s = [0]
    s = s + list(map(int, sys.stdin.readline().strip().split()))
    visit = [0 for i in range(n+1)]
    count = n

    for j in range(1, n+1):
        if visit[j] == 0:
            count -= bfs(j)

    print(count)