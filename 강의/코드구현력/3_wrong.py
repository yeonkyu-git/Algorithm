import sys
from itertools import combinations
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
cards = list(map(int, input().split()))
res = set()  # 중복 제거
count = 0
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(cards[i] + cards[j] + cards[m])
            count += 1
res = sorted(res, key=lambda x: -x)
print(res[k-1])





'''
cardsCom = list(combinations(cards, 3))
cardsSum = []
for i in range(len(cardsCom)):
    val = sum(cardsCom[i])
    if val not in cardsSum:
        cardsSum.append(sum(cardsCom[i]))

cardsSum = sorted(cardsSum, key=lambda x:-x)
print(cardsSum[k-1])
'''