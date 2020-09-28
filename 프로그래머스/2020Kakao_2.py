def solution(p):
    if p == '':
        return ''

    count_left = 0
    count_right = 0
    u = ''
    v = ''

    # 2. u, v 분리
    for i in range(len(p)):
        if p[i:i+1] == ')':
            count_left += 1
        else:
            count_right += 1

        if count_left == count_right:
            u = p[0:i+1]
            v = p[i+1:]
            break

    # 3. u가 올바른 괄호 문자열인지 아닌지
    temp = u

    while True:
        if temp.find('()') != -1:
            temp = temp.replace('()', '')
        else:
            break
    if temp == '':
        u += str(solution(v))
        return u
    else:
        u2 = u[1:len(u)-1]
        u2_temp = ''
        for i in range(len(u2)):
            if u2[i] == ')':
                u2_temp += '('
            else:
                u2_temp += ')'

        temp2 = '(' + str(solution(v)) + ')' + u2_temp
        return temp2



p = '()))((()'
print(solution(p))

# p[0] = ')'
# print(p)


