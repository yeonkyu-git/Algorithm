import sys
from collections import deque

def bfs(x, y, k):
    q.append([x, y])
    c1[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and c1[nx][ny] == 0:
                    c1[nx][ny] = k
                    q.append([nx, ny])

def bfs2():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if c2[nx][ny] == -1:
                    q.append([nx, ny])
                    c1[nx][ny] = c1[x][y]
                    c2[nx][ny] = 1 + c2[x][y]


def bfs3():
    min_number = sys.maxsize

    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if c1[x][y] != c1[nx][ny]:
                        if min_number > c2[x][y] + c2[nx][ny]:
                            min_number = c2[x][y] + c2[nx][ny]
    print(min_number)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
a = list()
nums = list()
c1 = [[0 for _ in range(n)] for _ in range(n)]
c2 = [[-1 for _ in range(n)] for _ in range(n)]
q = deque()

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
# 1단계 : 자신의 땅 번호 구별
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and c1[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

# 2단계 : c1과 c2가 확장해나갈 때 전체 Map 그리기
for i in range(n):
    for j in range(n):
        if c1[i][j] > 0:
            q.append([i, j])
            c2[i][j] = 0

bfs2()
# 3단계 : c1과 c2가 접하는 부분에서의 최솟값 구하기
#        1) c1에서 bfs를 하면서 서로 다른 부분 확인
#        2) c2에서 합침

bfs3()







