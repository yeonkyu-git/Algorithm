# 합병정렬 느낌 

import sys
sys.stdin = open("import.txt", "rt")

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

answer = []
p1 = 0
p2 = 0

# for _ in range(n+m):
#     if nList[p1] < mList[p2]:
#         answer.append(nList[p1])
#         p1 += 1
#         if p1 == n:
#             answer += mList[p2:]
#             break
#     else:
#         answer.append(mList[p2])
#         p2 += 1
#         if p2 == m:
#             answer += nList[p1:]
#             break

while p1 < n and p2 < m:
    if nList[p1] <= mList[p2]:
        answer.append(nList[p1])
        p1 += 1
    else:
        answer.append(mList[p2])
        p2 += 1

if p1 == n:
    answer += mList[p2:]
else:
    answer += nList[p1:]

print(' '.join(map(str, answer)))
