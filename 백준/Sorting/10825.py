n = int(input())
a = []

for i in range(n):
    a.append(list(input().split()))

a.sort(key= lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in a:
    print(i[0])

# for i in range(n):
#     for j in range(i+1, n):
#         b = int(a[i][1])
#         c = int(a[j][1])
#         if b < c:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
#         elif b == c:
#             d = int(a[i][2])
#             e = int(a[j][2])
#             if d > e:
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#             elif d == e:
#                 f = int(a[i][3])
#                 g = int(a[j][3])
#                 if f < g:
#                     temp = a[i]
#                     a[i] = a[j]
#                     a[j] = temp
#                 elif f == g:
#                     if a[i][0] > a[j][0]:
#                         temp = a[i]
#                         a[i] = a[j]
#                         a[j] = temp



