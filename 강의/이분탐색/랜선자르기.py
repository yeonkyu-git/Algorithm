import sys
sys.stdin = open('import.txt', 'rt')
k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))

lt = 1
rt = max(a)

while lt <= rt:
    mid = (lt + rt) // 2
    count = 0
    for val in a:
        count += val // mid

    if count >= n:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)
