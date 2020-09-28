import sys

a = [0 for i in range(26)]

for i in sys.stdin.readline().strip():
    a[ord(i) - ord('a')] += 1

print(' '.join(map(str,a)))