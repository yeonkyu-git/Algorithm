# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

N, C = map(int, input().split())
s = []

for _ in range(N):
    s.append(int(input()))

s.sort()

def binary_search(c, data):
    start = 1
    end = s[-1]
    result = 0

    while start <= end:
        mid = (start + end) // 2


