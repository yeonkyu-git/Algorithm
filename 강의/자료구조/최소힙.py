import sys
sys.stdin = open('imput.txt', 'rt')
heap = []

while True:
    k = int(input())
    if k == -1:
        break

    if k == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heap.pop(0))
    else:
        if heap:
            if k < heap[0]:
                heap.insert(0, k)
            else:
                heap.append(k)
        else:
            heap.append(k)

