import sys
import heapq as hq
sys.stdin = open('imput.txt', 'rt')
a = []
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if a:
            print(hq.heappop(a) * -1)
        else:
            print(-1)
    else:
        hq.heappush(a, -1 * n)