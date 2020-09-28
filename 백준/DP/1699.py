import math
n = int(input())

dp = [0 for i in range(n+1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    s = []
    for j in range(1, int(math.sqrt(i))+1):
        s.append(dp[i-j**2] + 1)
    dp[i] = min(s)

print(dp[n])
