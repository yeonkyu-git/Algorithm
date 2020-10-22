import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
prime_Number = [True for _ in range(n+1)]
answer = []
count = 0

for i in range(2, n+1):
    if prime_Number[i]:
        count += 1
        answer.append(i)
        for j in range(2*i, n+1, i):
            prime_Number[j] = False

print(count)
print(answer)