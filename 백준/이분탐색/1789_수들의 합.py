import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
index = 0
lastNumber = n
cnt = 0

while lastNumber > index:
  lastNumber -= index
  if lastNumber > index:
    cnt += 1
    index += 1

print(cnt)
