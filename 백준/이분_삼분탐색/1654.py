K, N = map(int, input().split())
s = []

for i in range(K):
    s.append(int(input()))
s.sort()

def solution(n, s):
    high = s[-1]
    low = 0
    result = 0

    while low <= high:
        mid = (high + low) // 2
        cnt = 0
        if mid == 0:
            return 1
        for val in s:
            cnt += val // mid

        if cnt >= n and mid > result:
            result = mid
        elif cnt < n:
            high = mid - 1
        else:
            low = mid + 1

    return result


print(solution(N, s))

