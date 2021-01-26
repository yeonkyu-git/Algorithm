import sys
sys.stdin = open('import.txt', 'rt')

def DFS(L, sum, tSum):
    global result
    if sum + (total - tSum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum + a[L], tSum + a[L])
        DFS(L+1, sum, tSum + a[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)