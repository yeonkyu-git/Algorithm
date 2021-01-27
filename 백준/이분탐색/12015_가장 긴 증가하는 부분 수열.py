import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip().split()))

table = [s[0]]

for idx in range(1, n):
  if table[-1] < s[idx]:
    table.append(s[idx])
  else:
    lt = 0
    rt = len(table)-1
    mid = 0
    while lt <= rt:
      mid = (lt+rt) // 2
      if table[mid] > s[idx]:
        rt = mid - 1
      elif table[mid] < s[idx]:
        lt = mid + 1
      else:
        break
    table[mid] = s[idx]

print(len(table))