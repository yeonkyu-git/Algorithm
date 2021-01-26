import sys
sys.stdin = open('import.txt', 'rt')

def DFS(L, sum):
    global res
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = sys.maxsize
    a.sort(reverse=True)
    DFS(0,0)
    print(res)