import sys
sys.stdin = open("import.txt", "rt")

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

s = nList + mList
print(sorted(s, key=lambda x : x))
