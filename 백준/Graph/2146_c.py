import sys
from collections import deque
sys.setrecursionlimit(200000)

s = [[-1, 0],[1, 0],[0, -1],[0, 1]]

def FindAnswer():
    minval = N*N
    for nowI in range(N):
        for nowJ in range(N):
            for i in range(4):
                nextI = nowI + s[i][0]
                nextJ = nowJ + s[i][1]
                if nextI >= 0 and nextI < N and nextJ >= 0 and nextJ < N:
                    if chk[nowI][nowJ] != chk[nextI][nextJ]:
                        if minval > dist[nextI][nextJ] + dist[nowI][nowJ]:
                            minval = dist[nextI][nextJ] + dist[nowI][nowJ]
    print(minval)

def Flood():
    while q:
        nowI, nowJ = q.popleft()
        for i in range(4):
            nextI = nowI + s[i][0]
            nextJ = nowJ + s[i][1]
            if nextI >= 0 and nextI < N and nextJ >= 0 and nextJ < N:
                if dist[nextI][nextJ] == -1:
                    q.append([nextI, nextJ])
                    dist[nextI][nextJ] = dist[nowI][nowJ] + 1
                    chk[nextI][nextJ] = chk[nowI][nowJ]


def BFS(i, j, cnt):
    q.append([i, j])
    chk[i][j] = cnt
    while q:
        nowI, nowJ = q.popleft()
        for i in range(4):
            nextI = nowI + s[i][0]
            nextJ = nowJ + s[i][1]
            if nextI >= 0 and nextI < N and nextJ >= 0 and nextJ < N:
                if chk[nextI][nextJ] != cnt and M[nextI][nextJ] == 1 :
                    q.append([nextI, nextJ])
                    chk[nextI][nextJ] = cnt

N = int(sys.stdin.readline())
M = list()
nums = list()
chk = [[0 for _ in range(N)] for _ in range(N)]
dist = [[-1 for _ in range(N)] for _ in range(N)]
q = deque()

for _ in range(N):
    M.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
for i in range(N):
    for j in range(N):
        if chk[i][j] == 0 and M[i][j] == 1:
            BFS(i, j, cnt)
            cnt += 1

for i in range(N):
    for j in range(N):
        if chk[i][j] > 0:
            q.append([i,j])
            dist[i][j] = 0

Flood()

FindAnswer()