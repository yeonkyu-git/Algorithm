import sys
a = sys.stdin.readline().strip()

s = [a[0]]
total = 0
for i in range(1, len(a)):
    if s and s[len(s)-1] != a[i] and a[i] == ')':
        if a[i-1] == '(':
            s.pop()
            total += len(s)
        else:
            s.pop()
            total += 1
    else:
        s.append(a[i])

print(total)