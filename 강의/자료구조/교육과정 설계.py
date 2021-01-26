import sys
from collections import deque
sys.stdin = open('imput.txt', 'rt')

# 입력값
classOrder = input()
n = int(input())
hOrder = []
for _ in range(n):
    hOrder.append(input())

def checkOrder(a,i):
    a = deque(a)
    cnt = 0  # 필수 과목 count

    while a:
        className = a.popleft()
        if className == classOrder[cnt]:
            cnt += 1

        # 검사
        if cnt == len(classOrder):
            print("#%d YES" % (i))
            return

    print("#%d NO" % (i))

for i in range(n):
    checkOrder(hOrder[i], i+1)
