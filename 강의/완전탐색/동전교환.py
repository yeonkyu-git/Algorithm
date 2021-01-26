import sys
sys.stdin = open('import.txt', 'rt')

def DFS(x, sum):
    global cnt
    if x >= cnt:
        return
    elif sum > m:
        return
    elif sum == m:
        if x < cnt:
            cnt = x
    else:
        for i in range(n):
            DFS(x+1, sum + coin[i])



if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(key=lambda x: -x)
    m = int(input())
    cnt = sys.maxsize
    DFS(0, 0)   # 동전의 개수, 합계
    print(cnt)