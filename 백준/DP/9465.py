n = int(input())

for i in range(n):
    k = int(input())
    s = []
    for index in range(2):
        s.append(list(map(int, input().split())))

    s[0][1] += s[1][0]
    s[1][1] += s[0][0]

    for index in range(2, k):
        s[0][index] += max(s[1][index-1], s[1][index-2])
        s[1][index] += max(s[0][index-1], s[0][index-2])

    print(max(s[0][k-1], s[1][k-1]))



