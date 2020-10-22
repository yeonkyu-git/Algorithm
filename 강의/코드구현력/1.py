n, k = map(int, input().split())
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1
    if count == k:
        print(i)
        break
else:
    print(-1)

# 파이썬에는 for ... else 구문 있음
# for 에서 break가 안걸릴 경우 else 구문 실행됨