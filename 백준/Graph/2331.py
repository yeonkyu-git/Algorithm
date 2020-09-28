import sys

def next_num(A, P):
    total = 0
    while (A != 0):
        total += (int(A % 10))**P
        A /= 10
    return total


A, P = map(int, sys.stdin.readline().strip().split())
s = [A]

while True:
    next_number = next_num(s[-1], P)
    if next_number in s:
        s.append(next_number)
        break
    else:
        s.append(next_number)

a = s.index(s[-1])
print(len(s[:a]))



