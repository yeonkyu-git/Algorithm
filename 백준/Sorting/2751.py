def merge_sorting(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    leftList = merge_sorting(a[:mid])
    rightList = merge_sorting(a[mid:])
    return merge(leftList, rightList)


def merge(leftList, rightList):
    s = []
    i=0
    j=0
    while i<len(leftList) and j<len(rightList):
        if leftList[i] <= rightList[j]:
            s.append(leftList[i])
            i += 1
        else:
            s.append(rightList[j])
            j += 1

    if i==len(leftList): s = s + rightList[j:len(rightList)]
    if j==len(rightList): s = s + leftList[i:len(leftList)]

    return s


a = [int(input()) for i in range(int(input()))]
a = merge_sorting(a)
print(*a, sep="\n")

