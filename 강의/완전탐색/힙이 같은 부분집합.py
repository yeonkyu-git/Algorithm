import sys
sys.stdin = open('import.txt', 'rt')

def dfs(x):
    if x == n:
        total = 0
        for i in range(0, n):
            if not visit[i]:
                total += s[i]
            else:
                total -= s[i]
        if total == 0:
            print('YES')
            sys.exit()  # 시스템 강제 종료
    else:
        dfs(x+1)
        visit[x] = True
        dfs(x+1)
        visit[x] = False

if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    visit = [False for _ in range(n)]
    dfs(0)
    print('NO')


