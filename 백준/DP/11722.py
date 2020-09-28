# n = int(input())
# a = list(map(int, input().split(' ')))
#
# dp = [0 for i in range(n)]
#
# dp[0] = 1
# # for i in range(1, n):
# #     s = []
# #     for j in range(0, i):
# #         if a[i] < a[j]:
# #             s.append(dp[j])
# #     if not s:
# #         dp[i] = a[i]
# #     else:
# #         dp[i] = max(s) + a[i]
#
# for i in range(1, n):
#     s = []
#     for j in range(0, i):
#         if a[i] < a[j]:
#             s.append(dp[j])
#     if not s:
#         dp[i] = 1
#     else:
#         dp[i] = max(s) + 1
#
# print(max(dp))



n = int(input())
s = list(map(int, input().split()))

dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if s[i] < s[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))