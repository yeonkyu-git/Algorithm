n = input()
s = []

for i in range(len(n)):
    s.append(n[i:])

s.sort(key= lambda x:(x))
print('\n'.join(s))