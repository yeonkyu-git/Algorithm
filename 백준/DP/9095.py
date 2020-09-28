"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

"""


# def solution(n):
#     dp = [0, 1, 2, 4]
#
#     for i in range(4, n+1):
#         dp.append(dp[i-1] + dp[i-2] + dp[i-3])
#
#     print(dp[n])





def recursion(k, n):
    if k == n:
        return 1
    elif k > n:
        return 0
    else:
        return recursion(k+1, n) + recursion(k+2, n) + recursion(k+3, n)


a = int(input())
for i in range(a):
    print(recursion(0, int(input())))
