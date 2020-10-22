import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

v = int(input())
s = [[] for _ in range(v+1)]
r1 = [0 for _ in range(v+1)]   # 1에서 가장 먼 정점 구하기
r2 = [0 for _ in range(v+1)]   # r1에서 값이 가장 큰 정점으로부터 가장 먼 정점 구하기


for i in range(v):
    path = list(map(int, sys.stdin.readline().split()))
    # 1+2i
    for j in range(1, len(path), 2):
        if path[j] != -1:
            s[path[0]].append([path[j], path[j+1]])

def dfs(start, r):
    for index, value in s[start]:
        if r[index] == 0:
            r[index] = r[start] + value
            dfs(index, r)


dfs(1, r1)
r1[1] = 0  # 1에서 시작했으므로 초기화
resultOneIndex = r1.index(max(r1))

# 두 번째 가장 먼 정점 구하기
dfs(resultOneIndex, r2)
r2[resultOneIndex] = 0  # resultOneIndex에서 시작했으므로 초기화
print(max(r2))


