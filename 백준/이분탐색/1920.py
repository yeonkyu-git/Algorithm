import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a = sorted(a, key=lambda x: x)


for i in range(m):
    lt = 0
    rt = n - 1
    temp = b[i]
    flag = False
    while lt <= rt:
        mid = (lt+rt) // 2

        if a[mid] > temp:
            rt = mid - 1
        elif a[mid] < temp:
            lt = mid + 1
        else:
            flag = True
            break

    if flag:
        print('1')
    else:
        print('0')
