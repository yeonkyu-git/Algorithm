n = input()

dp = [0 for i in range(len(n) + 1)]

dp[0] = 0
# 맨 앞자리 하나
if int(n[0]) != 0:
    dp[1] = 1

# 둘째 자리
if int(n[1]) != 0:
    dp[2] += 1
    if int(n[0:2]) >= 10 and int(n[0:2]) <=26:
        dp[2] += 1

# 셋째 자리 부터
for i in range(2, len(n)):
    # 안되는 경우 부터 판별
    if dp[i] == 0: dp[i+1] = 0    # 앞자리 dp 가 0이면 그 뒤로 다 0
    elif int(n[i]) == 0 and int(n[i-1:i+1]) > 26:
        dp[i+1] = 0
    elif int(n[i]) != 0:
        dp[i+1] += dp[i]
        if int(n[i-1:i+1]) <= 26 and int(n[i-1:i+1])  >= 10:
            dp[i+1] += dp[i-1]
    elif int(n[i-1:i+1]) <= 26 and int(n[i-1:i+1])  >= 10:
        dp[i+1] += dp[i-1]

#print(dp)
print(dp[len(n)]%1000000)




