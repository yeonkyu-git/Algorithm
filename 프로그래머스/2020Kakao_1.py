def solution(s):
    answer = len(s)  # len(s) 개 단위 만큼 자르면 그대로 이기 때문에 초기값을 len(s)로 설정
    for i in range(1, len(s)):
        count = 1
        new_str = ''
        last = s[0:i]
        next = ''
        for j in range(i, len(s), i):
            if j+i <= len(s):
                next = s[j:j+i]
                if last == next:
                    count += 1
                else:
                    if count == 1:
                        new_str += last
                        last = next
                    else:
                        new_str += str(count) + last
                        last = next
                        count = 1
            else:
                new_str += s[j:]

        if count == 1: new_str += last
        else: new_str += str(count) + last

        if answer > len(new_str):
            answer = len(new_str)
    return answer


s = "ababcdcdababcdcd"
print(solution(s))
