'''
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

이 문제는 한번 더 풀어볼 가치가 있다. 
'''


import sys
sys.stdin = open('import.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
lt = 0
rt = 1
tot = a[0]

while True:
    if tot<m:
        if rt<n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        count += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt+=1

print(count)