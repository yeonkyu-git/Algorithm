import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

lt = 1
rt = n ** 2
res = 0

while lt <= rt:
  mid = (lt+rt) // 2

  cnt = 0
  for i in range(1, n+1):
    cnt += min(mid // i, n)

  if cnt >= k:
    rt = mid - 1
    res = mid
  elif cnt < k:
    lt = mid + 1

print(res)