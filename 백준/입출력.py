import sys
# a,b=map(int,input().split())
# print(a+b)


# for i in range(int(input())):
#     print(sum(map(int, input().split((' ')))))


# while True:
#     try:
#         a,b = map(int, input().split(' '))
#         print(a+b)
#     except:
#         break

# for i in sys.stdin:
#     a,b = map(int,i.split(' '))
#     print(a+b)

# for i in range(int(input())):
#     print('Case #%d: %d'%(i+1, sum(map(int, input().split()))))



# for i in range(int(input())):
#     a,b = map(int, input().split())
#     print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))

# while True:
#     try:
#         str = input()
#         print(str)
#     except:
#         break

# print(sys.stdin.read())

# count = int(input())
# numbers = input()
# total = 0
#
# for i in range(count):
#     total += int(numbers[i])
# print(total)

# number = sum(map(int, input()))
# print(number)

# str = input()
# i = 0
# while True:
#     if len(str) < i:
#         break
#
#     print(str[i:i+10])
#     i += 10


# n = input()
# for i,a in enumerate(n):
#     if i != 0 and i%10 == 0: print('')
#     print(a,end='')


# for i in range(int(input()), 0, -1):
#     print(i)


# n = int(input())
#
# for i in range(1,10):
#     print('%d * %d = %d'%(n, i, n*i))


# a, b = map(int,input().split())
# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# days_str = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
#
# total_days = 0
# for i in range(1, a):
#     total_days += days[i-1]
# total_days += b
# print(days_str[total_days % 7])


# n = int(input())
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)


# print(sum(range(1, int(input()) +1 )))

# input()
# list = list(map(int, input().split(' ')))
#
# print(min(list))
# print(max(list))


# n = int(input())
# for i in range(1,n+1):
#     print('*' * i)


# n = int(input())
# for i in range(1, n+1):
#     print('*' * i + ' ' * 2 * (n-i) + '*' * i)
# for i in range(1, n):
#     print('*' * (n-i) + ' ' * 2 * i + '*' * (n-i))


# n = int(input())
# for i in range(1, n+1):
#     print(' ' * (n-i) + '*' * i)
#
# for i in range(1, n+1):
#     print(' ' * (i) + '*' * (n-i))


# n = int(input())
# for i in range(0, n):
#     print(' ' * i + '*' * (2 * (n-i) -1))
# for i in range(2, n+1):
#     print(' ' * (n-i) + '*' * (2 * i -1))

# n = int(input())
# for i in range(1, n+1):
#     print(' ' * (n-i), end='')
#     print('*', end='')
#     print(' *' * (i-1))

# n = int(input())
#
# for i in range(n):
#     if i == n-1:
#         print('*' * (2 * (i+1) - 1))
#     elif i == 0:
#         print(' ' * (n - i - 1) + '*')
#     else:
#         print(' ' * (n-i-1) + '*' + ' ' * (2 * i - 1) + '*')

#
# def solution(n, count):
#     if n == 1:
#         return counts.append(count)
#
#     if n % 3 == 0:
#         solution(n/3, count + 1)
#
#     if n % 2 == 0:
#         solution(n/2, count + 1)
#
#     solution(n - 1, count + 1)
#
#
# n = int(input())
# counts = []
# solution(n, 0)
# print(counts)
# print(min(counts))


# a = int(input())
# count = 0
# minimum = [a]
# def cal(temp_list):
#     list = []
#     for i in temp_list:
#         list.append(i-1)
#         if i%3 == 0:
#             list.append(i/3)
#         if i%2 == 0:
#             list.append(i/2)
#     return list
#
# while True:
#     if a == 1:
#         print(count)
#         break
#     temp = minimum[:]
#     minimum = cal(temp)
#     count += 1
#     if min(minimum) == 1:
#         print(count)
#         break







