import sys
from collections import deque
sys.stdin = open('import.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
a = deque(a)

answer = [0]
whichDi = ''

while a:
    # 요소가 하나 남았을 때
    if len(a) == 1:
        if answer[-1] < a[0]:
            answer.append(a[0])
        break

    leftNumber = a[0]
    rightNumber = a[-1]

    # 두 수 모두 answer보다 큰 경우 작은 값을 선택
    if leftNumber > answer[-1] and rightNumber > answer[-1]:
        if leftNumber < rightNumber:
            answer.append(a.popleft())
            whichDi += 'L'
        elif leftNumber > rightNumber:
            answer.append(a.pop())
            whichDi += 'R'
    else:
    # 두 수 중 하나만 answer 보다 큰 경우
        if leftNumber > answer[-1]:
            answer.append(a.popleft())
            whichDi += 'L'
        elif rightNumber > answer[-1]:
            answer.append(a.pop())
            whichDi += 'R'
        else:
            break  # 두 수 모두 answer 보다 작은 경우

print(len(answer)-1)
print(whichDi)