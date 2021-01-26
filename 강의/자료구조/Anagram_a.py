import sys
sys.stdin = open('imput.txt', 'rt')
a = input()
b = input()
sh = dict()

for x in a:
    sh[x] = sh.get(x, 0) + 1 # x라는 키값이 있으면 반환, 없으면 0 반환

for x in b:
    sh[x] = sh.get(x, 0) - 1

for x in a:
    if sh.get(x) != 0:
        print('NO')
        break
else:
    print('YES')


