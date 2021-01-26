import sys
sys.stdin = open('imput.txt', 'rt')
a = list(input())
s = []
cnt = 0

'''
for i in range(len(a)):
    if not s:
        s.append(a[i])
    else:
        if a[i] == ')':
            if a[i-1] == '(':
                s.pop()
                cnt += len(s)
            else:
                s.pop()
                cnt += 1
        else:
            s.append(a[i])
'''

## Class
for i in range(len(a)):
    if a[i] == '(':
        s.append(a[i])
    else:
        s.pop()
        if a[i-1] == '(':
            cnt += len(s)
        else:
            cnt += 1

print(cnt)

