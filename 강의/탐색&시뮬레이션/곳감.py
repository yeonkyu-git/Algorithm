import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if b == 0:   # 왼쪽으로 회전
        for _ in range(c):
            s[a-1].append(s[a-1].pop(0))
        # s[a-1] = s[a-1][c:] + s[a-1][:c]    -> 안되는 이유가 행의 길이 보다 더 많은 회전이 들어오면 틀리게 됨
    elif b == 1:   # 오른쪽으로 회전
        for _ in range(c):
            s[a-1].insert(0, s[a-1].pop())
        # s[a-1] = s[a-1][n-c:] + s[a-1][:n-c]

res = 0
start = 0
end = n
mid = n // 2
for i in range(n):
    if i < mid:
        res += sum(s[i][start:end])
        print(' '.join(map(str, s[i][start:end])))
        start += 1
        end -= 1
    else:
        res += sum(s[i][start:end])
        print(' '.join(map(str, s[i][start:end])))
        start -= 1
        end += 1


print(res)