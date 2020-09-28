# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
#
# dp = [0 for i in range(n)]
#
# if n > 2:
#     dp[0] = a[0]
#     dp[1] = a[0] + a[1]
#     dp[2] = max(a[0], a[1]) + a[2]
# elif n < 2:
#     dp[0] = a[0]
# else:
#     dp[0] = a[0]
#     dp[1] = a[0] + a[1]
#
# for i in range(3, n):
#     dp[i] = max(dp[i-3] + a[i-1] + a[i], dp[i-2] + a[i])
#
# print(dp[n-1])


n = int(input())
s = [0]
for i in range(n):
    s.append(int(input()))
s.append(0)

dp = [0]
dp.append(s[1])
if n > 1:
    dp.append(s[1] + s[2])

for i in range(3, n+1):
    dp.append(max(dp[i-2]+s[i], dp[i-3] + s[i] + s[i-1]))

print(dp[n])

