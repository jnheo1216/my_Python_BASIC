
# first class

# first-class citizen (1급 시민)

# 프로그램의 구성요소(개체)가 다음의 조건을 만족하면
# first-class citizen 이라고 부름

# 1. 구성요소가 변수나 데이터구조의 속성으로 저장될 수 있어요
# 2. 함수의 인자로 전달될 수 있어요
# 3. 함수의 결과로 리턴될 수 있어요

# 아주 쉽게 생각하면
# 우리가 사용하는 일반숫자타입의 데이터
100
# 함수의 인자로 넘겨줄 수 있고 함수의 결과로 리턴될 수 있어
# 그러니까 일반숫자는 일급시민입니다

# 우리가 사용하는 객체(class로부터 파생된 instance)
# 파이썬에서 사용되는 객체는 1급시민의 조건을 만족 => 1급객체

# 파이썬의 함수는 ?
# 만약 1급시민의 조건을 만족한다면 일급 함수(first class function)라고 부름!
# python은 1급 함수를 지원하는 언어에요!!
# => 함수를 runtime으로 생성이 가능

# -1. 함수를 변수에 저장할 수 있어요!

def my_add(x, y):
    return x + y

print(my_add)
f = my_add
print(f(100, 200))  # 가능

# -2. 함수를 다른 함수의 인자로 전달할 수 있어요!

def my_add2(x, y):
    return x + y
def my_sub2(x, y):
    return x - y

def my_operation(func, arg_list):  # 끼워넣어
    result = []
    for (tmp1, tmp2) in arg_list:
        result.append(func(tmp1, tmp2))  # 마치 조립하듯이 # 유연성이 늘어나요
    return result

data = [(1, 2), (3, 4), (5, 6)]
print(my_operation(my_add2, data))
print(my_operation(my_sub2, data))

# -3. 함수를 다른 함수의 리턴값으로 사용할 수 있어요!
#     => Closure 라는 개념도 필요

def addMaker(x):  # x는 지역변수로 함수가 호출되면 생성되고 함수가 종료되면 사라짐

    def my_add_maker(y):  # 함수안의함수 ㄷㄷ
        return x + y

    return my_add_maker

# print(addMaker()())  # 모양이 신기함

add_5 = addMaker(5)
add_10 = addMaker(10)
print(add_5(100))
print(add_10(100))  # 함수를 동적으로 만들 수 있음 ㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷ

#########################################################################

# Closure
# first class function(일급함수)의 개념을 이용하여
# 스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미해요!
# 클로저는 데이터를 저장한 레코드. 스코프 안의 변수가
# 소멸되어도 그에 대한 접근을 클로저를 통해서 할 수 있어요!








###

