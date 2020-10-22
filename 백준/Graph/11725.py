import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n = int(input())

s = [0 for i in range(n+1)]  # 런 타임 범인
a = [[] for i in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)


def dfs(x):
    if not a[x]:
        return
    m = a[x].copy()
    for i in m:
        if s[i] == 0:
            s[i] = x
            dfs(i)

def dfs_a(start, a, s):
    for i in a[start]:
        if s[i] == 0:
            s[i] = start
            dfs_a(i, a, s)


dfs_a(1, a, s)
for i in range(2, n+1):
    print(s[i])
