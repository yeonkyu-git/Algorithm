import sys
sys.stdin = open('import.txt', 'rt')

s = [list(map(int, input().split())) for _ in range(7)]

count = 0
for i in range(7):
    for j in range(3):
        a = []
        b = []
        for k in range(5):
            a.append(s[i][k+j])
            b.append(s[k+j][i])
        c = a.copy()
        a.reverse()
        d = b.copy()
        b.reverse()
        if a == c:
            count += 1

        if b == d:
            count += 1

print(count)