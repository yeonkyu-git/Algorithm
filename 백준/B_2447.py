def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return list(matrix)


star = ["***", "* *", "***"]
n = int(input())
k = 0

# 입력된 정수가 3의 몇승+1 인지 파악
while n > 3:
    n /= 3
    k += 1

print(k)

for i in range(k):
    star = stars(star)

print('\n'.join(star))