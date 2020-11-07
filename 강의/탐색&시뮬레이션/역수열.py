import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
a = [0] + list(map(int, input().split()))
answer = [0 for i in range(n+1)]

print(a)

for i in range(1, n+1):
    cnt = 0
    for j in range(n+1):
        if answer[j] == 0:
            cnt += 1
            if cnt-1 == a[i]:
                answer[j] = i
                break
print(answer)
answer.pop()

print(' '.join(list(map(str, answer))))



