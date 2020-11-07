import sys
sys.setrecursionlimit(100000)

def Count(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target > numCards[mid]:
        return Count(mid+1, end, target)
    elif target < numCards[mid]:
        return Count(start, mid-1, target)
    else:
        return numCards[start:end+1].count(target)

n = int(sys.stdin.readline())
numCards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
numCardsTwo = list(map(int, sys.stdin.readline().split()))

numCards.sort()
answer = []

for i in range(m):
    lt = 0
    rt = n-1
    target = numCardsTwo[i]
    answer.append(Count(lt,rt,target))

print(' '.join(list(map(str, answer))))