t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    inputList = list(map(int, input().split()))
    inputList = inputList[s-1:e]
    inputList = sorted(inputList, key=lambda x: x)
    print("#%d %d" % (i+1, inputList[k-1]))


