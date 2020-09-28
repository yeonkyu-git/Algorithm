N, K = map(int, input().split(' '))

dp = [[1 for i in range(201)] for j in range(201)]


for i in range(2, N+1):
    for j in range(2, i+1):
        total = 0
        for k in range(j - 2, i + 1):
            total += dp[k][j - 1] * (j - 1)
        dp[i][j] = total


print(dp[N][K] % 1000000000)