import sys
sys.stdin = open('import.txt', 'rt')

def DFS(x):
    global cnt
    if x == m:
        cnt += 1
        for var in ch:
            print(var, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if i not in ch:
                ch.append(i)
                DFS(x+1)
                ch.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = []
    cnt = 0
    DFS(0)
    print(cnt)
