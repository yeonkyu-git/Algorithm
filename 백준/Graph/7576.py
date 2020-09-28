import sys
from collections import deque

def bfs (x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    while q:
        x, y = map(int, q.popleft())
        for dir in range(4):
            new_x = x + dx[dir]
            new_y = y + dy[dir]

            if new_y >= 0 and new_x >= 0 and new_x < n and new_y < m:
                if visit[new_x][new_y] == 0 and s[new_x][new_y] == 0:
                    s[new_x][new_y] = 1


m, n = map(int, sys.stdin.readline().strip().split())
s = [[0 for i in range(m)] for j in range(n)]
visit = [[0 for i in range(m)] for j in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 0

for i in range(n):
    s[i] = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and s[i][j] == 1:
            bfs(i, j)


for i in range(n):
    for j in range(m):
        print(visit[i][j], end=' ')
    print()
