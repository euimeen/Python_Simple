# 튜플(Tuple)
# - List와 대부분 동일
# - 시퀀스 자료형
# - index 사용(slicing 가능)
# - packing unpacking 가능
# - immutable(생성 된 후 변경 불가)
# - 정렬 불가능
# - ()사용 ()생략 가능
print("="*100)
a = [1,2,3]  # List
b = (1,2,3)  # Tuple
c = 1,2,3    # Tuple

a[0]=99
print(a)
# b[0]=99  #Tuple 값 변경 불가
# print(b)

# 튜플 원소가 1개인 경우!
a = (1,2,3)  # tuple
b= 1,2,3  # tuple
c=(1)   # tuple
d=1     # int
e = 1,  # tuple
print(type(b))
print(type(d))
print(type(e))

# a와 b를 교환 하는 코드
# JAVA, C 에서의 Swap
# temp = a
# a = b
# b = temp
# a = 5
# b = 8


# python
a,b = b,a  # tuple의  packing, unpacking
print(a) # 8
print(b) # 5

# 3. 세트(Set) ex) 복주머니
# - 수학의 집합 개념
# - 순서 없음(index 없음, 정렬 불가)
# - 중복값 허용 하지 않음(중요)
# - {} 사용
# - 멤버함수: union(), intersection(), difference()
# * Set는 대부분 중복값 제거 활용

set_a = {1,1,1,2,2,3,4,5}
print(set_a)

# 중복값 제거 활용 방법
# - a List의 중복값을 제거
a = ["A", "A", "B", "B", "B"] #List type
# a = set(a)  # ()안의 값을 set type으로 변경
# a = list(a) # ()안의 값을 list type으로 변경
# List -> Set(중복값 제거) -> List
print(list(set(a)))

# 4.딕트(dict) ex)복주머니
# - 순서가 없음(인덱스 없음, 정렬 불가)
# - {key:value} -> key, value 1pair
# - key(중복 불가), value(중복 가능)
# - key를 통해서만 value 접근 가능
# - 멤버함수: update(), get(), keys(), values(), items()

# 사전(dict) type의 중요성!
# - 외부에서 데이터를 주고 받는 표준 구격 : JSON
# - {"id":"abc123","pw":"@!123", "name":"체리"}
# - Python의  dict == JSON

dict_a = {"korea":"seoul",
          "Canada":"Ottaws",
          "USA":"Washington D.C"}
print(dict_a)
import pprint
pprint.pprint(dict_a)


# update(): dict와 dict병합
a ={"a":1,
    "b":2}
b={"b":3,
   "c":5}
a.update(b)
print(a)  # 병합시 중복 key는  입력값(b)이 우선

# pop(key) : dict 원소를  key를 통해 삭제
abc = {"a":1, "b":2, "c":3}
c = abc.pop("a")
print(abc)
print(c)

# in() : ()안의 key값이  존재 확인
print("c" in abc)
print("f" in abc)

# get(): 값 접근
# list, tuple, dict접근
# -> 컬레션[index or key]
# -> ex: a[1], ["c"]
# print(abc["f"])  # key가 없으면 error 발생
print(a.get("f"))  # key가 없으면 none 출력(error x)

# keys(), values(), items()
print(a)
print(a.keys())    # key만 추출
print(a.values())  # value만 추출
print(a.items())   # (key, value) 추출

print(list(a.keys()))  # 활용 방법


# clear() : dict 초기화
print(abc)
abc.clear()
print(abc)

a = {}
#
#
#