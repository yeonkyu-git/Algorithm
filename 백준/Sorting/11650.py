# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로,
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.




def merge_sorting(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sorting(a[:mid])
    right = merge_sorting(a[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0; j = 0
    s = []
    while i < len(left) and j < len(right):
        if left[i][0] > right[j][0]:
            s.append(right[j])
            j += 1
        elif left[i][0] == right[j][0]:
            if left[i][1] > right[j][1]:
                s.append(right[j])
                j += 1
            else:
                s.append(left[i])
                i += 1
        else:
            s.append(left[i])
            i += 1

    if i == len(left): s = s + right[j:]
    elif j == len(right): s = s + left[i:]

    return s


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


# a.sort(key=lambda x: (x[0], x[1]))

for i in merge_sorting(a):
    print(i[0], i[1])