import sys
sys.stdin = open('import.txt', 'rt')

l = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort(key=lambda x: -x)

for _ in range(m):
    a[0] -= 1
    a[-1] += 1
    a.sort(key=lambda x: -x)

print(a[0] - a[-1])
