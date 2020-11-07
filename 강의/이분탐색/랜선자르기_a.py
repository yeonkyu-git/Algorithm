import sys
sys.stdin = open('import.txt', 'rt')

def Count(len):
    cnt = 0
    for x in line:
        cnt += x // len
    return cnt


k, n = map(int, input().split())
line = []
res = 0
max_Line = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    max_Line = max(max_Line, tmp)

lt = 1
rt = max_Line

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

