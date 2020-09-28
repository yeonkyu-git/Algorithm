import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push':
        a.append(order[1])
    elif order[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif order[0] == 'size':
        print(len(a))
    elif order[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a) - 1])


