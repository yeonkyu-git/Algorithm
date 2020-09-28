n = input()
new_n = ''

for i in n:
    if i.isupper():
        s = (ord(i) + 13 - ord('A')) % 26
        new_n += chr(s + ord('A'))
    elif i.islower():
        s = (ord(i) + 13 - ord('a')) % 26
        new_n += chr(s + ord('a'))
    else:
        new_n += i

print(new_n)

