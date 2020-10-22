import sys
sys.setrecursionlimit(10 ** 9)

v = int(sys.stdin.readline())
s1 = [[] for _ in range(v+1)]
r1 = [0 for _ in range(v+1)]   # 1에서 가장 먼 정점 구하기
r2 = [0 for _ in range(v+1)]   # r1에서 가장 큰 값으로부터 먼 정점 구하기

for i in range(v-1):
    path = list(map(int, sys.stdin.readline().split()))
    s1[path[0]].append([path[1], path[2]])
    s1[path[1]].append([path[0], path[2]])

def dfs(start, r):
    for index, value in s1[start]:
        if r[index] == 0:
            r[index] = r[start] + value
            dfs(index, r)

dfs(1, r1)
r1[1] = 0
farIndex = r1.index(max(r1))
dfs(farIndex, r2)
r2[farIndex] = 0
print(max(r2))
