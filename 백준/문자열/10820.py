import sys

while True:
    try:
        n = input()
        if n == '':
            break

        lowercase_count = 0
        uppercase_count = 0
        number_count = 0
        space_count = 0

        for i in n:
            a = ord(i)
            if a >= ord('a') and a <= ord('z'):
                lowercase_count += 1
            elif a >= ord('A') and a <= ord('Z'):
                uppercase_count += 1
            elif a >= ord('0') and a <= ord('9'):
                number_count += 1
            else:
                space_count += 1

        print(lowercase_count,uppercase_count,number_count,space_count)
    except EOFError:
        break


