import sys

sys.stdin = open('import.txt', 'rt')

n, c = map(int, sys.stdin.readline().strip().split())
a = []
for i in range(n):
  a.append(int(sys.stdin.readline()))

a.sort(key=lambda x: x)

lt, rt, pos = 0, a[n - 1], 0
res = 0

while lt <= rt:
  mid = (lt + rt) // 2
  cnt = 1
  pos = 0
  for i in range(1, n):
    if a[i] - a[pos] >= mid:
      cnt += 1
      pos = i

  if cnt >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)
