n = int(input())
a = list(map(int, input().split()))

dp_f = [0 for i in range(n)]  # 정방향
dp_b = [0 for i in range(n)]  # 역방향

# 정방향
dp_f[0] = 1
for i in range(1,n):
    for j in range(0, i):
        if a[i] > a[j] and dp_f[i] < dp_f[j]:
            dp_f[i] = dp_f[j]
    dp_f[i] += 1

# 역방향
dp_b[n-1] = 1
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j] and dp_b[i] < dp_b[j]:
            dp_b[i] = dp_b[j]
    dp_b[i] += 1

dp = []
for i in range(n):
    dp.append(dp_f[i]+dp_b[i]-1)

print(max(dp))

