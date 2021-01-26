import sys

sys.stdin = open('imput.txt', 'rt')
a, b = map(int, input().split())
a = list(map(int, str(a)))
stack = []

for x in a:
    while stack and b > 0 and stack[-1] < x:
        stack.pop()
        b -= 1
    stack.append(x)

if b != 0:
    stack = stack[:-b]

print(''.join(map(str, stack)))

