import sys
from collections import deque
import copy

# 각각의 섬 구하기
def bfs1():
    while q1:
        a, b = map(int, q1.popleft())
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if s[x][y] == 1 and visit1[x][y] == 0:
                    visit1[x][y] = 1
                    q1.append([x, y])
                    q2.append([x, y])

# 각각의 섬에서 출발
def bfs2(count_part):
    count = 1000
    while q2:
        a, b = map(int, q2.popleft())
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and visit1[x][y] == 0 and visit2[x][y] != count_part:
                if s[x][y] != 1:
                    q2.append([x, y])
                    visit2[x][y] = count_part
                    s[x][y] = s[a][b] + 1
                elif s[x][y] == 1:
                    visit2[x][y] = count_part
                    if count > s[a][b] - 1:
                        print("qwe")
                        count = s[a][b] - 1
        if count != 1000:
            break
    return count


n = int(sys.stdin.readline())
s = []
q1 = deque()
q2 = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().strip().split())))
visit1 = [[0 for i in range(n)] for j in range(n)]
visit2 = [[0 for i in range(n)] for j in range(n)]

count_min = 1000
count_part = 1

for i in range(n):
    for j in range(n):
        if s[i][j] == 1 and visit1[i][j] == 0:
            visit1[i][j] = 1
            q1.append([i, j])
            q2.append([i, j])
            bfs1()
            temp_count = bfs2(count_part)
            if count_min > temp_count:
                count_min = temp_count
            print("asd")
            count_part += 1

print(count_min)








