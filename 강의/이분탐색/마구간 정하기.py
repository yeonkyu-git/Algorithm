import sys
sys.stdin = open('import.txt', 'rt')

def LenBetween(mid):
    last = m[0]
    cnt = 1
    for i in range(1, len(m)):
        if m[i] - last >= mid:
            cnt += 1
            last = m[i]
    return cnt

n, c = map(int, input().split())
m = []
for _ in range(n):
    m.append(int(input()))

m.sort()
lt = min(m)
rt = max(m)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2

    countOfHorse = LenBetween(mid)
    if countOfHorse < c:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1
print(res)

