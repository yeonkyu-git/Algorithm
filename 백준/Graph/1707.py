'''
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
'''
from collections import deque
import sys

k = int(sys.stdin.readline().strip())
def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):
    v, e = map(int, sys.stdin.readline().strip().split())
    isTrue =True
    s = [[] for i in range(v + 1)]
    bi = [0 for i in range(v + 1)]   # visit


    for j in range(e):
        a, b = map(int, sys.stdin.readline().strip().split())
        s[a].append(b)
        s[b].append(a)

    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                isTrue = False
                break

    print("YES"if isTrue else "NO")




#
# def bfs(x, y):
#     if s[x] == 'N':
#         if s[y] == 'N':
#             s[x] = 'R'
#             s[y] = 'B'
#         else:
#             s[x] = 'R' if s[y] == 'B' else 'B'
#     else:
#         if s[y] == 'N':
#             s[y] = 'R' if s[x] == 'B' else 'B'
#         else:
#             if s[x] == s[y]:
#                 return False
#     return True
#
#
#
# n = int(sys.stdin.readline().strip())  # 테스트 케이스 개수
#
# for i in range(n):
#     a, k = map(int, sys.stdin.readline().strip().split())
#     s = ['N' for i in range(20001)]
#     visit = [0 for i in range(20001)]
#
#     flag = True
#     for j in range(k):
#         x, y = map(int, sys.stdin.readline().strip().split())
#         if not bfs(x, y):
#             flag = False
#             break
#     if flag:
#         print('YES')
#     else:
#         print('NO')


'''
Test case
11
3 1
2 3

3 2
1 3
2 3

4 4
1 2
2 3
3 4
4 2

3 2
2 1
3 2

4 4
2 1
3 2
4 3
4 1

5 2
1 5
1 2

5 2
1 2
2 5

4 3
1 2
4 3
2 3

4 4
2 3
1 4
3 4
1 2

3 3
1 2
2 3
3 1

2 1
1 2

YES O
YES O
NO  O
YES O
YES O
YES O
YES O
YES 
YES  
NO  
YES 

'''