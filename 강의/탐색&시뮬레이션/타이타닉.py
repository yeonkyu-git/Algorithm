import sys
from collections import deque   # 시간복잡도 많이 낮아짐

sys.stdin = open('import.txt', 'rt')

n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort(key=lambda x:-x)
w = deque(w)

boatCount = 0
while w:
    boatCount += 1
    firstMan = w.popleft()
    if w:
        if m - firstMan >= w[-1]:
            w.pop()

print(boatCount)