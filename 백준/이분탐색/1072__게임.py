import sys
from math import floor
#sys.stdin = open('import.txt', 'rt')

x, y = map(int, sys.stdin.readline().strip().split())  # 게임 횟수, 이긴 게임
z = floor(100 * y / x)

lt = 0
rt = 1000000000
res = 0

if z >= 99:
  print(-1)
else:
  while lt <= rt:
    mid = (lt + rt) // 2

    new_x = x + mid
    new_y = y + mid
    if floor(100 * new_y / new_x) > z:
      res = mid
      rt = mid - 1
    else:
      lt = mid + 1

print(rt + 1)



