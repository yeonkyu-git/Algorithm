n,k = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a, key= lambda x:(x))
print(a[k-1])