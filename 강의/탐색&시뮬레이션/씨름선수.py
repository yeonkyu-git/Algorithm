import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
people = []
for _ in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

people.sort(key=lambda x: (-x[1], -x[0]))
answer = 0
height = 0

for h, w in people:
    if height < h:
        answer += 1
        height = h

print(answer)
