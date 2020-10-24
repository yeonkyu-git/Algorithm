import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
total = 0
mid = n // 2

for i in range(n):
    if i <= mid:
        total += sum(a[i][mid - i:mid + i + 1])
    else:
        total += sum(a[i][i - mid:n - i + mid])

print(total)


res = 0
s = e = n // 2
for i in range(n):
    if i < mid:
        res += sum(a[i][s:e+1])
        s -= 1
        e += 1
    else:
        res += sum(a[i][s:e+1])
        s += 1
        e -= 1

print(res)