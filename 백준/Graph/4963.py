from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append([x,y])
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    visit[x][y] = 1
    while q:
        x, y = map(int, q.popleft())
        for dir in range(8):
            new_x = x + dx[dir]
            new_y = y + dy[dir]
            if new_x >= 0 and new_y >= 0 and new_x < a and new_y < b:
                if visit[new_x][new_y] == 0:
                    visit[new_x][new_y] = 1
                    if s[new_x][new_y] == 1:
                        q.append([new_x, new_y])

    return 1

while True:
    b, a = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break

    s = [[0 for i in range(b)] for j in range(a)]
    visit = [[0 for i in range(b)] for j in range(a)]
    count = 0
    for i in range(a):
        s[i] = list(map(int, sys.stdin.readline().strip().split()))

    for x in range(a):
        for y in range(b):
            if visit[x][y] == 0 and s[x][y] == 1:
                count += bfs(x,y)

    print(count)
