import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in a:
    try:
        dic[i] += 1
    except :
        dic[i] = 1

for i in b:
    if dic.get(i) != None:
        print(dic.get(i), end=' ')
    else:
        print('0', end=' ')