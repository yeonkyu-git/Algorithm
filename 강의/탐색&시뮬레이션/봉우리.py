import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
# s.insert(0, [0]*n)
# s.append([0]*n)
# for x in s:
#     x.insert(0, 0)
#     x.append(0)
#
# for x in s:
#     print(x)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

for i in range(n):
    for j in range(n):
        for dir in range(4):
            new_x = i + dx[dir]
            new_y = j + dy[dir]
            if 0 <= new_x < n and 0 <= new_y < n:
                if s[i][j] <= s[new_x][new_y]:
                    break
        else:
            count += 1
print(count)

