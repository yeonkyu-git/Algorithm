# n = int(input())  # 구매하려는 카드 개수
# p = list(map(int, input().split(' ')))  #  index+1 = 팩에 들어있는 카드의 개수
#
# dp = [0 for i in range(n)]
# dp[0] = p[0]
#
# for i in range(1, n):
#     max_price = 0
#     for j in range(0, i):
#         temp_price = dp[j] + p[i-j-1]
#         if max_price < temp_price: max_price = temp_price
#
#     if max_price < p[i]:
#         max_price = p[i]
#     dp[i] = max_price
#
# print(dp[n-1])


n = int(input())
d = [0] * (n+1)
p = [0] + list(map(int, input().split()))
d[1] = p[1]

for i in range(2, n+1):
    for j in range(0, i):
        if d[i] < d[j] + p[i-j]:
            d[i] = d[j] + p[i-j]
print(d)