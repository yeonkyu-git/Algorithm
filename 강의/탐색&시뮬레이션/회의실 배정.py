import sys
sys.stdin = open('import.txt', 'rt')

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))   # 시작시간, 끝나는 시간

# a.sort(key=lambda x: (x[1], x[0]))
a = sorted(a, key=lambda x: (x[1], x[0]))  # 끝나는 시간 순으로 정렬
answer = 1  # 강의 수
lastFinishTime = a[0][1]

for i in range(1, n):
    if lastFinishTime <= a[i][0]:
        answer += 1
        lastFinishTime = a[i][1]

print(answer)


