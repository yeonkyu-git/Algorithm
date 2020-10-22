import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
ans = list(map(int, input().split()))
total = 0
count = 0

for i in range(n):
    if ans[i] == 1:
        count += 1
        total += count
    else:
        count = 0

print(total)