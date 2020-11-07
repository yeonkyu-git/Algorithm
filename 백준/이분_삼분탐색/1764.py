import sys
n, m = map(int, sys.stdin.readline().split())
noListen = []
answer = []
cnt = 0

for _ in range(n):
    noListen.append(sys.stdin.readline().strip())

noListen.sort()
noListenLen = len(noListen)-1

for _ in range(m):
    person = sys.stdin.readline().strip()
    lt = 0
    rt = noListenLen
    while lt <= rt:
        mid = (lt + rt) // 2
        if noListen[mid] < person:
            lt = mid + 1
        elif noListen[mid] > person:
            rt = mid - 1
        else:
            cnt += 1
            answer.append(person)
            break

answer.sort()
print(cnt)
print('\n'.join(answer))


