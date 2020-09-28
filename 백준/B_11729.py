# def hanoi (n, k):
#     if n == 1:
#         print(str(k)+'  3')
#         return
#     s = 2 if k == 1 else 1
#     print(str(k)+' '+str(s))
#     print(str(k)+' 3')
#     hanoi(n-1, s)


def hanoi2(n, from_pos, to_pos, aux_pos):
    if n == 1:
        move.append([from_pos, to_pos])
        return

    # 원반 n-1개를 aux_pos로 이동
    hanoi2(n-1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반을 목적지로 이동
    move.append([from_pos, to_pos])
    hanoi2(n-1, aux_pos, to_pos, from_pos)


move = []
n = int(input())
k = hanoi2(n, 1, 3, 2)

print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))
