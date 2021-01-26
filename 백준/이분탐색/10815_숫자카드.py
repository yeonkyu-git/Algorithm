import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a = sorted(a, key=lambda x: x)

for i in range(m):
    lt, rt, tmp, flag = 0, n-1, b[i], False
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] < tmp:
            lt = mid + 1
        elif a[mid] > tmp:
            rt = mid - 1
        else:
            flag = True
            break
    if flag:
        print("1 ", end='')
    else:
        print("0 ", end='')

