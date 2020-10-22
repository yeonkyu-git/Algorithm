t = int(input())

n = [[] for _ in range(41)]
n[0] = [1, 0]
n[1] = [0, 1]

for i in range(2, 41):
    n[i] = [n[i-1][0] + n[i-2][0], n[i-1][1] + n[i-2][1]]

for _ in range(t):
    inputNumber = int(input())
    print(' '.join(list(map(str, n[inputNumber]))))

