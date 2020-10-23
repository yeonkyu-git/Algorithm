'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''

import sys
sys.stdin = open("import.txt", "rt")

n = int(input())

def backString(str):
    bkstr = ""
    for i in range(len(str)):
        bkstr += str[len(str) - i -1]
    return bkstr

for i in range(n):
    str = input().lower()
    # bkstr = backString(str)

    if str == str[::-1]: # str[::-1] 거꾸로 출력함
        print("asd")

    for j in range(len(str) // 2):
        if str[j] != str[-j -1]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

