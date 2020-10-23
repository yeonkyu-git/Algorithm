import sys
sys.stdin = open("import.txt", "rt")

s = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    temp = s[a:b+1]
    # for j in range(a, b+1):
    #     s[j] = temp[-1-j+a]

    for i in range((b-a+1) // 2):
        s[a + i], s[b - i] = s[b - i], s[a + i]
        
print(' '.join(map(str, s[1:])))
