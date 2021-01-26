import sys
from collections import deque

sys.stdin = open('imput.txt', 'rt')
n = int(input())
writeWord = []
poemWord = []

for _ in range(n):
    writeWord.append(input())
for _ in range(n-1):
    poemWord.append(input())

writeWord = deque(writeWord)

while writeWord:
    word = writeWord.popleft()
    if word not in poemWord:
        print(word)
        break

