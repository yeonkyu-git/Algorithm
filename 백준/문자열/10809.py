import sys
a = [-1 for i in range(26)]
str_input = sys.stdin.readline().strip()

for i in str_input:
    index_a = ord(i) - ord('a')
    if a[index_a] == -1:
        a[index_a] = str_input.index(i)

print(' '.join(map(str, a)))