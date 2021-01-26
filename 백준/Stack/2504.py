import sys
a = sys.stdin.readline()
stack = []

for i in range(len(a)):
    if a[i] == '(' or a[i] == '[':
        stack.append(a[i])
    elif a[i] == ')':
        if a[i-1] == '(':
            stack.pop()
            value = 2
        else:
            value = int(stack.pop()) * 2
            stack.pop()
        while stack and stack[-1].isdecimal():
            value += int(stack.pop())
        stack.append(str(value))
    elif a[i] == ']':
        if a[i-1] == '[':
            stack.pop()
            value = 3
        else:
            value = int(stack.pop()) * 3
            stack.pop()
        while stack and stack[-1].isdecimal():
            value += int(stack.pop())
        stack.append(str(value))

if len(stack) == 1:
    print(''.join(stack))
else:
    print(0)
