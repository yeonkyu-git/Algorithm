import sys
sys.stdin = open('import.txt', 'rt')

n, m = map(int, input().split())
s = list(map(int, input().split()))

s = sorted(s, key=lambda x: x)
start = 0
end = len(s)-1

def binary_search(start, end, target):
    mid = (start + end) // 2
    if s[mid] > target:
        binary_search(start, mid-1, target)
    elif s[mid] < target:
            binary_search(mid+1, end, target)
    else:
        if s[mid] == s[mid - 1]:
            binary_search(start, end-1, target)
        else:
            print(mid+1)

binary_search(0, len(s)-1, m)

