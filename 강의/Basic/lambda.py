'''
람다 함수
'''

def plus_one (x):
    return x+1


plus_two = lambda x: x+2
print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_one, a)))   # map(함수, 자료)
print(list(map(lambda x: x+2, a)))   # 람다 함수가 유용할 때