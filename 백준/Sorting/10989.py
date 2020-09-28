n = int(input())
a = [0 for i in range(n+1)]

for i in range(n):
    a[int(input())] += 1

for i in range(n+1):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)


