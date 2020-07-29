#
# python에서 module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
# 다른 파이썬 프로그램에서 불러와서 사용할 수 있어요

# module을 사용하는 이유는 코드의 재사용성과 관리목적

# python 모듈은 크게 2가지가 있음
# - C언어로 구성된 binary module
# - python언어로 구성된 일반 module

# module을 사용하기 위해 사용하는 keyword : import
# module도 파이썬 입장에서는 객체로 관리된다

import sys

print(sys.path)  # 리스트 형식임

sys.path.append("c:/python_data")  # 모듈을 저장할 폴더를 지정

# 모듈 만들기 (파이썬 파일 하나 생성)

# 만들었으니 써보자

import module1  # as m1

print(module1.my_pi)
print(module1.my_adder(10, 20))
# print(m1.my_pi)
# print(m1.my_adder(10, 20))

from module1 import my_adder  # 이 함수 당장 땡겨와
print(my_adder(10, 20))

from module1 import *  # 싸그리 싹 다 땡겨와
print(my_pi)

# package
## c:/python_data/test_module에 module1.py를 갖다넣자

import test_module.module1 as mymodule1

print(mymodule1.my_adder(20, 20))
