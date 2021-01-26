'''
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
'''

import sys
sys.stdin = open('imput.txt', 'rt')

a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        number = []
        res = 0
        for _ in range(2):
            number.append(stack.pop())
        num1 = int(number[0])
        num2 = int(number[1])

        if x == '+':
            res = num1 + num2
        elif x == '-':
            res = num2 - num1
        elif x == '*':
            res = num1 * num2
        else:
            res = num2 / num1

        stack.append(res)

print(res)




