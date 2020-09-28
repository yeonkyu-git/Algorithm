import sys

def push_front(x):
    a.insert(0,x)
def push_back(x):
    a.append(x)
def pop_front():
    if not a:
        return -1
    else:
        return a.pop(0)
def pop_back():
    if not a:
        return -1
    else:
        return a.pop()
def size():
    return len(a)
def empty():
    if not a:
        return 1
    else:
        return 0
def front():
    if not a:
        return -1
    else:
        return a[0]
def back():
    if not a:
        return -1
    else:
        return a[len(a) - 1]


n = int(sys.stdin.readline().strip())
a= []

for i in range(n):
    order = list(map(str, sys.stdin.readline().strip().split()))

    if order[0] == 'push_front':
        push_front(int(order[1]))
    elif order[0] == 'push_back':
        push_back(int(order[1]))
    elif order[0] == 'pop_front':
        print(pop_front())
    elif order[0] == 'pop_back':
        print(pop_back())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())

