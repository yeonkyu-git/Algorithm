import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))
avg = round(sum(s) / n)
min = float('inf')

for idx, x in enumerate(s):  # idx : index , x : value
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)
