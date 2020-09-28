# 선택 정렬
def sorting(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    return numbers


num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(input()))

numbers = sorting(numbers)
print('\n'.join(map(str, numbers)))
