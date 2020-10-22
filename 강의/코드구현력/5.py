import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
s = {}
res = []

for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j not in s.keys():
            s[i+j] = 1
        else:
            s[i+j] += 1

maxValue = max(s.values())
for key, val in s.items():
    if val == maxValue:
        res.append(key)

res.sort()
print(' '.join(list(map(str, res))))