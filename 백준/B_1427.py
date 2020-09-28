def sorting (numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    before_list = numbers[:mid]
    after_list = numbers[mid:]
    before_list = sorting(before_list)
    after_list = sorting(after_list)
    return merge(before_list, after_list)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


num = input()
list = list(map(int, num))

list = sorting(list)
print(''.join(map(str, list)))