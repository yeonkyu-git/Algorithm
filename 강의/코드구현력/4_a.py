import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))
avg = round(sum(s) / n)   # 파이썬에서는 round_half_even 방식 : half 지점에 있으면 짝수쪽으로 간다.
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
