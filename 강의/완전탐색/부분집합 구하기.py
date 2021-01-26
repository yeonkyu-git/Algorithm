import sys
sys.stdin = open('import.txt', 'rt')

def dfs(x):
    if x == n+1:
        for i in range(1, n+1):
            if not visit[i]:
                print(i, end=' ')
        print()
    else:
        dfs(x+1)
        visit[x] = True
        dfs(x+1)
        visit[x] = False


if __name__ == "__main__":
    n = int(input())
    visit = [False for _ in range(n+1)]
    dfs(1)