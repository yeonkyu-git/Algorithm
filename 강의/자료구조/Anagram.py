import sys

sys.stdin = open('imput.txt', 'rt')
a = input()
b = input()
dic = {}

for val in a:
    if dic.get(val):
        dic.update({val: dic.get(val) + 1})
    else:
        dic[val] = 1

for val in b:
    if dic.get(val):
        if dic.get(val) == 1:
            dic.pop(val)
        else:
            dic.update({val: dic.get(val) - 1})
    else:
        print('NO')
        break

if not dic:
    print('YES')

