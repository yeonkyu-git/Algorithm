from collections import deque
n, m = map(int, input().split())
s = []
q = deque()
visit = [[0 for i in range(m)] for j in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    s.append(list(input()))


def bfs():
    while q:
        a, b = map(int, q.popleft())
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if visit[x][y] == 0 and int(s[x][y]) == 1:
                    s[x][y] = int(s[a][b]) + 1
                    visit[x][y] = 1
                    q.append([x, y])

        for i in s:
            for j in i:
                print(j, end=' ')
            print()
        print()


q.append([0,0])
visit[0][0] = 1
bfs()



