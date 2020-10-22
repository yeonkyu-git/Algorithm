import sys
def dfs(v):
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 1
    while queue:
        v = queue.pop(0)
        for i in range(1, n+1):
            if visit[i] == 0 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 1


n, k = map(int, sys.stdin.readline().strip().split())
s = [[0] * (n+1) for i in range(1001)]
visit = [0 for i in range(1001)]
answer = 0

for i in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    s[x][y] = 1
    s[y][x] = 1

for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        answer += 1

print(answer)


# 안녕하세요 깃
