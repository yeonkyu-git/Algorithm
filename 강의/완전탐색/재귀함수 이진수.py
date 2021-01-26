import sys
sys.stdin = open('import.txt', 'rt')
n = int(input())

def binary(n):
    if n < 2:
        return str(n)
    else:
        return binary(n // 2) + str((n % 2))

print(binary(n))