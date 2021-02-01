# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우 : global을 사용
a = 0

def fuc():
  global a
  a += 1

for i in range(10):
  fuc()
print(a)

# 람다 표현식
print((lambda a, b: a+b)(3,7))

