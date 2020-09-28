# n = int(input())
# s = list(map(int, input().split(' ')))
# dp = [0 for i in range(n)]
# dp[0] = s[0]
# for i in range(1, n):
#     a = []
#     for j in range(i-1, -1, -1):
#         if s[i] > s[j]:
#             a.append(dp[j])
#     if not a:
#         dp[i] = s[i]
#     else:
#         dp[i] = max(a) + s[i]
#
# print(max(dp))


n = int(input())
s = list(map(int, input().split(' ')))

dp = [0 for i in range(n)]
dp[0] = s[0]

for i in range(1, n):
    for j in range(i):
        if s[i] > s[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += s[i]

print(max(dp))

