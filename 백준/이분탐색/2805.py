import sys
sys.stdin = open('import.txt', 'rt')

n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = max(s)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    tot = 0  # 총 자른 나무 길이
    for i in range(n):
        if s[i] > mid:
            tot += (s[i] - mid)
        if tot >= m:
            res = mid
            lt = mid + 1
            break

    if tot < m:
        rt = mid - 1

print(res)