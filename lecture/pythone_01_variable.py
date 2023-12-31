# 주석(comment): 메모, 실행x
#  글씨체: D2Coding
# 1.출력 함수(print)
# - ()안의 값을 출력
# - 변수 값 확인 용도로 많이 사용
print("Hello Python")
# 문자열 타입(string type)
#- python: ''or "" -> string
# - c, java: ''(char), ""(string)
print("=" * 200)
#참고: escape code
#-문법 : \(역 슬래쉬)+@
#예) \n: 한줄 개행, \t: 탭(8칸 공백)
print("=" * 200)
print("Hello \nPython")
print("Hello \tPython")
# 회사: 항상 신기술, 새로나온 코드 기법 사용 x
 # 3.8
# 3.9 새로운 기법 추가!

# 2. 자료형(type)
# - python의 모든 자료형은 객체(object)
# java 정수형: byte, short, int, long
# Python 정수형: int
# 문자열(string) : "hello", "hi"
# 정수형(int): 3,-1,0
# 실수형 (float): 3.14, 0.0. -2.2
# 논리형(boolean): True, False

# 설명: 동일한 type에서 다양한 종류의 자료형을 사용하는 이유?
# - 메모리(저장공간)를 효율적으로 사용하기 위해서!
#  - 대부분 만들어진지 오래 된 언어는 다양한 종류의 자료형 사용!
#  - 자료형은 저장 할 수 있는 크기의 범위가 지정
# - 가정: int(-10000 ~10000)
# - 가정: short(-100~ 100)
# - 특정 값 : 0~9-> 어떤 type을 사용하면 효율적일까요?

# 3. 동적 타이핑 언어(Dynamic Typing Language)
# -JAVA :int num =4;
# - python: num =4(Type 지정 x)
# -코드가 실행될 때 자동으로 Type을 지정
# -type() 함수: ()안의 값을 type을 확인할 때 사용
print("="*200)
print(type("ABC"))
print(type(3.14))
print(type(5))

# 4.형 변환(Type CASTING)
# - type casting을 사용하면 값을 원하는 자료형으로 변환 가능
# -1 )int(): 정수형으로 변환
# -2)float(): 실수형으로 변환
# -3)str(): 문자열형으로 변환
print("="*200)
# - "Hi" --> float(), int() 불가!
# 문자열 실수형 : "3.14" 가능
# 문자열 정수형: "5" 가능
int_a =3
float_b="9"
str_int_c="9"
str_float_d ="9.2"
# 큰자료형 -> 작은 자료형으로 변환할 때 주의!
# 정수형(3)-> 실수형(3.0)
print(float(int_a))
# 정수형(3)-> 문자열("3")
# 정수형(3)-> 실수형(3.0)
# 실수형(3.14) -> 정수형(3) # 주의 !(팡리 손실 생김)
# 문자열 정수형("3") -> 정수형(3)
# 문자열 정수형("3") -> 실수형(3.0)
# 문자열 실수형("3.14")->정수형(3) error
# print(int(str_float_d))
# 문자열 실수형("3.14")-> 실수형(3.14)

# 5. None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값울 갖지 않게 하고 생성할 때 사용
# -  기타 언어의 Null 과 같은 의미로 사용
print("="*200)

# C, JVAV: 변수 생성 -> int num;
# Python: 변수 생성 -> num (Error)
# python: 변수 생성 -> num = None
student_name = None  #절대 사용 금지!
student_name = ""  #적극 권장!

# "Null Pointer Exception"

# 기본 자료형(Primitive Type): 변수에 값이 그대로 저장
# - int num = 4;
# 객체 자료형(Reference Type): 변수에 값이 위치한 "주소"가 저장
# - String name = "10";

# *JAVA 와 C: 기본, 객체 둘 다 사용
# * Python: 객체만 사용

# 6.변수(Variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간
print("="*200)
num= 4
num= 10
print(num) # 출력: 10

# - 변수 생성 및 초기화
# 문법: num = 5
#  * num: "num" 변수 생성
# * 대입연산자(=): 우측의 값을 좌측에 저장
# * 동등연산자(==): Equal
# *  초기화: 초기 변수를 생성하면 쓰레기 파일들이 존재
# 변수에 값을 대입한면 공간이 초기화 되고 값만 저장!


