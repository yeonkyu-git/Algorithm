n = int(input())
d = {}

for case in range(n):
    tmp = int(input())
    if tmp in d:
        d[tmp] += 1
    else:
        d[tmp] = 1

d = sorted(d.items(), key= lambda x:( -x[1], x[0]))
print(d[0][0])