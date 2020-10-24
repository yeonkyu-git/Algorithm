import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
sumOne = 0
sumTwo = 0

# 행 열 대각선 합 구하기
for i in range(n):
    sumRow = 0  # 열
    sumCol = 0  # 행
    for j in range(n):
        sumRow += a[j][i]
        sumCol += a[i][j]

        if i == j:
            sumOne += a[i][j]
            sumTwo += a[i][n-i-1]
    maxLayer = sumRow if sumRow > sumCol else sumCol
    if maxLayer > maxSum:
        maxSum = maxLayer

# 대각선 구하기
print(max(maxSum, sumOne, sumTwo))