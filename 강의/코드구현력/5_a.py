import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
cnt = [0] * (n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
maxVal = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == maxVal:
        print(i, end=' ')