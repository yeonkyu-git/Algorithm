import sys

n = int(sys.stdin.readline().strip())


## 쉽게 풀기
for i in range(n):
    a = sys.stdin.readline().strip()
    while '()' in a:
        a = a.replace('()', '')

    if a == '':
        print('YES')
    else:
        print('NO')



## 스택으로 풀기
for i in range(n):
    s = []
    a = sys.stdin.readline().strip()
    for j in a:
        if s and s[len(s)-1] != j and j == ')':
            s.pop()
        else:
            s.append(j)

    if s:
        print('NO')
    else:
        print('YES')