# round 함수
a = 0.3 + 0.6
a = round(a, 1)  # round(실수형 데이터, 반올림하고자 하는 위치__소수점 첫째 자리: 1)
print(a)

# 리스트 컴프리헨션
## 리스트를 초기화하는 방법 중 하나
a = [i for i in range(20) if i % 2 == 1]
b = [i ** 2 for i in range(1, 10)]
print(b)
## 2차원 배열을 초기화할 때 매우 유용하다
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
## list의 메소드 중에 insert, remove 는 시간 복잡도가 O(N)이고, append는 O(1) 이다.
## 파이썬에서 특정 원소의 값을 모두 제거 하는 방법은 아래와 같다.
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]  # remove_set에 포함되지 않는 다면 result에 넣겠다.
print(result)

# 튜플 자료형
## 리스트와 비슷하지만 가장 큰 차이점은 튜플은 한 번 선언된 값을 변경할 수 없다.
## 튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다.

# 사전 자료형
## 일반적으로 키-쌍 구조이기 떄문에, 검색 및 수정에 있어 O(1)의 시간복잡도를 갖는다.
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
## 사전 자료형에서 특정 원소가 있는지 검사할 때, __ 리스트나 튜플에서도 적용 가능
if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")
## 사전 자료형 관련 함수
### 키 데이터만 담은 리스트
key_list = data.keys()
### 값 데이터만 담은 리스트
data_list = data.values()
print(list(key_list))
print(data_list)
### 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])


# 집합 자료형
## 1. 중복을 허용하지 않는다. / 2. 순서가 없다.  / 3. 키는 없고 값 데이터만 있다. / 4. 검사 시간 복잡도는 O(1)
## 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적이다.
data = {1, 2, 3, 4, 5, 6, 7}
print(data)
## 집합 자료형의 연산
### 합집합 교집합 차집합
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
## 집합 자료형 관련 함수
### dict과 마찬가지로 수정 및 삭제는 시간복잡도가 O(1)이다.
data = {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 제거
data.remove(3)
print(data)