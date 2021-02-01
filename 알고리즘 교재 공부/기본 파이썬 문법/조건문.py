# 조건문에서 아무것도 처리하고 싶지 않을 때 pass문을 이용한다.
score = 85
if score >= 80:
  pass
else:
  print("asd")

# 조건부 표현식을 이용할 수 있다.
result = "Success" if score >= 80 else "Fail"
print(result)