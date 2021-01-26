import sys
from collections import deque
sys.stdin = open('imput.txt', 'rt')

n, m = map(int, input().split())
people = list(map(int, input().split()))
people = deque(people)
count = 0

while people:
    number = people.popleft()
    if number < max(people):
        people.append(number)
    else:
        if m == 0:
            print(count + 1)
            break
        else:
            count += 1

    if m == 0:
        m = len(people) - 1
    else:
        m -= 1
