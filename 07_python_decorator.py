# Decorator

# Decorator 의 사전적의미는 장식가, 도배업자
# 파이썬에서 decorator는 기존의 코드에 여러가지 기능을 추가하는
# 파이썬 구문이라고 이해하면 편해요

# Closure
# 지역변수에 있는 값을 저장하는곳 # 나중에 쓰려고
# first class function(일급함수)
# 1. 파이썬의 함수는 변수에 저장할 수 있어요!
# 2. 함수의 인자로 함수를 이용할 수 있어요! ==> Decorator
# 3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있어요! ==> Closure


# def my_outer_func(func):
#
#     def my_inner_func():
#         func()
#
#     return my_inner_func
#
#
# def my_func():
#     print("my_func() 함수가 호출됨!")
#
#
# decorated_my_func = my_outer_func(my_func)  # 함수 그 자체를 넘겨주는거임 # 괄호 ㄴㄴ
# decorated_my_func()
# my_func()  # 둘 다 동일하게 실행함!!

import time


def my_outer_func(func):

    def my_inner_func():
        print("{} 함수수행시간을 계산합니다.".format(func.__name__))  # 함수의 이름을 알기휘한 매직펑션
        start = time.time()  # 1970년 1월 1일 0시0분0초 = 0
        func()
        end = time.time()
        print("함수수행시간은 {} 입니다..".format(start - end))

    return my_inner_func


@my_outer_func  # 이걸 데코레이트 시켜서 실행할거야 # 이게 데코레이트
def my_func():
    print("my_func() 함수가 호출됨!")


# decorated_my_func = my_outer_func(my_func)  # 함수 그 자체를 넘겨주는거임 # 괄호 ㄴㄴ
# decorated_my_func()
my_func()  # 추가적인 내용을 넣고싶은데 고치면 안될때

#########################################################################


def print_user_name(*args):  # 인자로 들어온 사람의 이름을 출력
    #args는 tuple로 받아요!   # 별표가 있으면 몇개들어올지 고민 안해도 됨
    for name in args:
        print(name)
print_user_name("홍길동", "신사임당")  # 이렇게도 하고
print_user_name("홍길동", "신사임당", "김철수")  # 이렇게도 할 수 있게


def print_user_name2(**kwargs):  # 별표가 두개 ㄷㄷ
    # 얘는 dict로 받아요!!
    for key in kwargs.keys():
        print(kwargs.get(key))
print_user_name2(name1="홍길동", name2="신사임당")
#{"name1": "홍길동", "name2: "신사임당"}


## Decorator에 대해 한가지 더 알아봐요

def my_outer2(func):
    def my_inner2(*args, **kwargs):  # 어떻게 들어오건 다 받을 수 있게
        print("데코레이터 시작")
        func(*args, **kwargs)
        print("데코레이터 끝")
    return my_inner2  # 어쨌거나 저쨌거나 데코레이터의 형식임

@my_outer2
def my_func2():
    print("이것은 소리없는 아우성")

@my_outer2
def my_add2(x, y):
    print("두 수의 합은 : {}".format(x+y))


my_func2()
my_add2(10, 20)










print("hello world!")