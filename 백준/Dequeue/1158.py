from collections import deque

a,b = map(int,input().split())

# a = [i+1 for i in range(a)]
# s = []
#
# index = 0
# while a:
#     index = (index+b-1) % len(a)
#     s.append(a.pop(index))
#
# print("<" + ', '.join(list(map(str, s))) + ">")


dq = deque([i+1 for i in range(a)])
res = []

while dq:
    dq.rotate(-b+1)
    res.append(dq.popleft())

print("<" + ', '.join(list(map(str, res))) + ">")