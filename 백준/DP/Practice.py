n = int(input())
s = [0] + list(map(int, input().split()))

dp = [0 for i in range(n+1)]
dp[1] = s[1]

for i in range(2, n+1):
    for j in range(0, i):
        if dp[i] < dp[j] + s[i-j]:
            dp[i] = dp[j] + s[i-j]

print(dp[n])
