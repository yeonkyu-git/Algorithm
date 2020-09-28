def solution(n, lost, reserve):
    answer = 0

    reserve_temp = reserve
    # 여벌 옷을 가져온 자기 자신이 잃어 버린 경우 Check
    for person in reserve_temp:
        if person in lost:
            lost.pop(lost.index(person))
            reserve.pop(reserve.index(person))

    for person in reserve:
        if person+1 in lost:
            lost.pop(lost.index(person + 1))
        elif person-1 in lost:
            lost.pop(lost.index(person-1))

    answer = n - len(lost)
    return answer


n = 7
lost = [2,3,4]
reserve = [1,2,3,6]

print(solution(n,lost,reserve))
