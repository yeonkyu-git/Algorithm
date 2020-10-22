N, M = map(int, input().split())  # M : Target
s = list(map(int, input().split()))
s.sort()

def binary_search(n, data):
    high = s[-1]
    low = 0
    result = 0

    while low <= high:
        get_tree = 0
        mid = (low + high) // 2
        for val in data:
            if val > mid:
                get_tree += (val - mid)   # mid 높이로 자른 후 가져갈 나무 길이

        if n <= get_tree:
            low = mid + 1
            result = mid

        if n > get_tree:
            high = mid - 1

    return result

print(binary_search(M,s))