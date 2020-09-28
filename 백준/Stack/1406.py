import sys

stk1 = list(sys.stdin.readline().strip())
stk2 = []
n = int(sys.stdin.readline().strip())

right = ''
for i in range(n):
    order = list(map(str, sys.stdin.readline().strip().split()))
    if order[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif order[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif order[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif order[0] == 'P':
        stk1.append(order[1])

stk2.reverse()
stk = stk1 + stk2
print(''.join(stk)) 