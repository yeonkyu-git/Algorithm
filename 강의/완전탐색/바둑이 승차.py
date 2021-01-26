import sys
sys.stdin = open('import.txt', 'rt')
'''
답은 맞으나 시간이 너무 오래 걸림 
'''
def DFS(idx, total):
    global maxW
    if total >= c:
        return
    elif idx == n:
        if maxW < total:
            maxW = total
    else:
        DFS(idx+1, total + w[idx])
        DFS(idx+1, total)


if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    maxW = 0
    for _ in range(n):
        w.append(int(input()))
    DFS(0, 0)
    print(maxW)