N = int(input())
a = list(map(int, input().split()))   # 상근이가 가지고 있는 숫자 카드
M = int(input())
b = list(map(int, input().split()))   # 상근이가 가지고 있는 숫자 카드인지 구해야 할 정수

a.sort()

def binary_sort(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == data[mid]:
            return data.count(data[mid])
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for val in b:
    print(binary_sort(val, a), end=' ')
