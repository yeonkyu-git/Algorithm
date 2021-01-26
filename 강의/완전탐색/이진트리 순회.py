import sys
sys.stdin = open('import.txt', 'rt')

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2 + 1)


def DFS2(v):
    if v > 7:
        return
    else:
        DFS2(v*2)
        print(v, end=' ')
        DFS2(v*2 + 1)


def DFS3(v):
    if v > 7:
        return
    else:
        DFS3(v*2)
        DFS3(v*2 + 1)
        print(v, end=' ')


if __name__ == "__main__":
    DFS(1)
    print()
    DFS2(1)
    print()
    DFS3(1)