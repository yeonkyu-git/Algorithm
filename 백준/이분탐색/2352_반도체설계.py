import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
semi = list(map(int, sys.stdin.readline().strip().split()))

table = [semi[0]]

for idx in range(1, n):
  if table[-1] < semi[idx]:
    table.append(semi[idx])
  else:
    lt = 0
    rt = len(table)-1
    mid = 0
    while lt <= rt:
      mid = (lt+rt) // 2
      if table[mid] > semi[idx]:
        rt = mid - 1
      elif table[mid] < semi[idx]:
        lt = mid + 1
      else:
        break
    table[mid] = semi[idx]

print(len(table))