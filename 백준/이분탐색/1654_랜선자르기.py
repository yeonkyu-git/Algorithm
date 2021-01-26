import sys
sys.stdin = open('import.txt', 'rt')

a, b = map(int, sys.stdin.readline().split())
s = []
for i in range(a):
    s.append(int(sys.stdin.readline()))

lt, rt, res = 0, max(s), 0
while lt <= rt:
    mid = (lt + rt) // 2
    tot = 0
    if mid == 0:
        lt = mid + 1
        res = 1
        break

    for i in range(a):
        tot += s[i] // mid
        if tot >= b:
            res = mid
            lt = mid + 1
            break
    if tot < b:
        rt = mid - 1

print(res)

