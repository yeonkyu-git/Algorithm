def sorting(numbers):
    for end in range(1, len(numbers)):
        for i in range(end, 0, -1):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]

    return numbers


num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(input()))

numbers = sorting(numbers)
print('\n'.join(map(str, numbers)))