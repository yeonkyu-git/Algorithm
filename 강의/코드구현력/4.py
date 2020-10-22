import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
s = [0] + list(map(int, input().split()))
v = [0 for _ in range(n+1)]
avg = round(sum(s) / (len(s) - 1))

# 수학점수에서 평균점수 차감
for i in range(1, len(s)):
    v[i] = abs(s[i] - avg)

m = min(v[1:])
print(avg, end=' ')
# 가장 높은 점수의 학생 + 가장 빠른 번호
for i in range(1, len(s)):
    if s[i] == avg + m:
        print(i)
        break
else:
    for i in range(1, len(s)):
        if s[i] == avg-m:
            print(i)
            break


