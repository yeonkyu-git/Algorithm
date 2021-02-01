# 1. 내장함수
## sum, min, max
## (1) eval  : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3+7)*7")
print(result)

## (2) sorted
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50), ('김연규', 35)], key= lambda x: (x[1], x[0]))
print(result)

## (3) itertools : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
### permutations, combinations 가 유용하다. (순열, 조합)
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 순열
print(result)
result2 = list(combinations(data, 2)) # 조합
print(result2)
result3 = list(product(data, repeat=3))  # 순열 + 원소를 중복해서 뽑는다.
print(result3)
result4 = list(combinations_with_replacement(data, 2)) # 조합 + 원소를 중복해서 뽑는다.
print(result4)


## (4) heapq
### 힙 기능을 위해 heapq 라이브러리 사용한다.
### heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
### 힙에 원소를 삽입할 때는 heapq.heappush(), 꺼낼 때는 heapq.heappop()


## 힙정렬 구현 : 보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은' 원소이다.
import heapq
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

## 최대힙 구현 : 파이썬에서는 최대힙을 제공하지 않아서 아래와 같이 구현한다.
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


## (5) bisect
