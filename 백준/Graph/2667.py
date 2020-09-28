from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    count = 1
    while q:
        x, y = map(int, q.popleft())
        for dir in range(4):
            new_x = x + dx[dir]
            new_y = y + dy[dir]
            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < n :
                if visit[new_x][new_y] == 0:
                    visit[new_x][new_y] = 1
                    if int(s[new_x][new_y]) == 1:
                        count += 1
                        q.append([new_x, new_y])

    return count

n = int(sys.stdin.readline())
s = [[0 for j in range(n)] for i in range(n)]
visit = [[0 for j in range(n)] for i in range(n)]
answer = []

for i in range(n):
    s[i] = list(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and int(s[i][j]) == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer = sorted(answer, key=lambda x : x)
print('\n'.join(list(map(str, answer))))


