import sys
sys.stdin = open('import.txt', 'rt')

n, m = map(int, input().split())
songLen = list(map(int, input().split()))
maxx = max(songLen)
lt = 0
rt = sum(songLen)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2  # DVD 용량
    cnt = 1  # DVD 개수
    sumOfSong = 0

    if mid >= maxx:
        for x in songLen:
            if sumOfSong + x > mid:
                cnt += 1
                sumOfSong = x
            elif sumOfSong + x <= mid:
                sumOfSong += x
        if cnt <= m:
            res = mid
            rt = mid - 1
    else:
        lt = mid + 1

print(res)