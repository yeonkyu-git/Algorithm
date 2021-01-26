import sys
sys.stdin = open('import.txt', 'rt')

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())


def binary():
    # 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
    if sum(s) <= m:
        return max(s)

    # 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
    lt = min(s)
    rt = max(s)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        tot = 0
        for var in s:
            if var <= mid:
                tot += var
            else:
                tot += mid
        if tot <= m:
            if res < mid:
                res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return res

print(binary())