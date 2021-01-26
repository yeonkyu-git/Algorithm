import sys
sys.stdin = open('import.txt', 'rt')


def DFS(x, s):
    if x > n:
        return

    if len(s) == m:
        print(' '.join(list(map(str, s))))

    else:
        s.append(x)
        DFS(x, s)
        s.pop()
        DFS(x + 1, s)
        s.append(x)
        DFS(x + 1, s)
        s.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    DFS(0, [])