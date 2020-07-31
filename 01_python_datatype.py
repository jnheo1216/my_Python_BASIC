# 1. 주석
# <= 한줄짜리주석
""" 이게 여러줄짜리 주석 """
''' 이거도 주석임 '''
# 주석 한꺼번에 붙이기 : ctrl + /

# 2. 파이썬의 키워드
import keyword
print(keyword.kwlist)
#어떤 키워드가 있나 확인해본거임

# 3. 변수생성, 삭제
my_val = 100
print(my_val)

# 4. 변수를 삭제할수있어
del my_val
#print(my_val)

# 5. Python의 데이터 타입(data type)
# 파이썬의 built-in data type 6개
# - Numeric(숫자형)
# - Sequence (순서가있는거)
# - text Sequence (문자열)
# - set
# - mapping
# - bool

#############################################################################################

# - 1. Numeric(숫자형)

# int
# float
# complex
a = 100  #정수
b = 3.14159  #실수
c = 1 + 2j  #복소수
d = 0o34  # 8진수 int
e = 0xAB  # 16진수 int

my_result = 3 / 4
print(my_result)  # 0이 아니라 0.75 나옴. 파이썬특)

my_result = 10 % 3
print(my_result)  # 나머지 구하는 법

my_result = 10 // 3
print(my_result)  # 몫만 구하는 법

#데이터타입을 알고싶어
print(type(c))  # type : 해당 변수의 데이터타입 리턴해주는 함수

########################################################################################

# - 2. Text sequence type(str) 문자열

# 다른 언어는 문자와 문자열을 구분함. 근데 파이썬은 다!! 문자열임
# 다른 언어는 보통 문자 '' 문자열 ""
# 파이썬은 문자열을 표현할때 ('', "")
# aa = "hello"
# bb = "k"
# cc = 'py'

#문자열연산
first = "haha"
second = "hoho"

print(first + second)  # hahahoho
print(first + str(10))  # haha10 #str을 붙여줘야함
print(first * 3)  # hahahahahaha

#indexing
my_var = "Hello"
print(my_var[0])  # 0 1 2 3 4
print(my_var[-1])  #로꾸꺼 # -5 -4 -3 -2 -1

#slicing
print(my_var[0:3])  # Hel # 0이상 3미만
my_var = "이것은소리없는아우성!!"
print(my_var[0:3])  # 이것은 # 한글이나 영어나 차이없음
print(my_var[3:])
print(my_var[0:-1])  #처음부터 마지막하나 빼고

# in, not in 연산자
myStr = "This is a sample Text"
print("sample" in myStr)  # True
print("sample" not in myStr)  # False

# formatting
# myStr = "나는 사과를 %d개 가지고 있어요!" %3
# print(myStr) #3이 저기 d자리에 박힘
# num_apple = 11
# myStr = "나는 사과를 %d개 가지고 있어요!" % num_apple
# print(myStr)

# 문자열 formatting은 아래의 표현을 주로 사용!
num_apple = 10
myStr = "나는 사과를 {}개 가지고 있어요!".format(num_apple)
print(myStr) # 중괄호에 숫자 박힘
num_apple = 10
myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요!".format(num_apple, 20)
print(myStr) # 중괄호에 숫자 박힘, 바나나숫자에 20

# 문자열 method를 이용해서 문자열 처리를 할 수 있음
myStr = "cocacola"
print(len(myStr)) # 문자열의 길이를 알아보기위해 len() 함수 사용
print(myStr.count('c'))  # str의 method인 count() 사용 # 몇개?
print(myStr.find('o'))  # 어디에?
myStr = "    myHobby"
print(myStr.upper())
print(myStr.lower())
print(myStr.strip())  # 빈칸 없애줌

###########################################################################################

# - 3. Sequence type

# list
# 임의의객체(데이터)를 순서대로 저장하는 집합 자료임
# java의 ArrayList 느낌
# list는 Literal로 표현될때 [] (대괄호로 표현)
my_list = []
print(type(my_list))
my_list = list()
my_list = [1, 2, 3.14, 'Hello', [5, 6, 7], 100]

#indexing과 slicing 가능
print(my_list[-2])  # [5,6,7] # 인덱싱
print(my_list[4:5])  # [5,6,7] # 위에거랑 결과는 같아보이지만 다름 # 이건 1개짜리 리스트임 # slicing이니까
print(my_list[4][1])  # 6

# list 연산
aa = [1, 2, 3]
bb = [4, 5, 6]
print(aa + bb)  # [1,2,3,4,5,6] # 연결임
print(aa * 3)  # [1,2,3,1,2,3,1,2,3]

aa[0] = [7, 8, 9]
print(aa)  # [[7, 8, 9], 2, 3] #리스트의 요소를 바꾸는 것
aa[0:1] = [7, 8, 9]
print(aa)  # [7, 8, 9, 2, 3] # 리스트를 바꾸는 것

aa = [1, 2, 3]
aa.append(4)
print(aa)  # [1,2,3,4] # 끝에다 추가하는 method
aa.append([5, 6, 7])
print(aa)  # [1,2,3,4,[5,6,7]

#정렬하기
my_list = ["홍길동", "아이유", "강감찬", "신사임당", "Kim"]
result = my_list.sort() # 리스트를 오름차순으로 정렬 # 유니코드순 # 원본이 바뀜
print(my_list)

# tuple
# list 는 대괄호[]표현, tuple은 소괄호()로 표현
aa = (1, 2, 3)  # 일반적인 tuple
# 만들어지면 내용 변경이 안됨!
# 변하면 안되는 것은 이걸로 만듬
aa = (3, )  # 요소가 1개만 존재하는 tuple표현법
aa = 1, 2, 3  #tuple은 괄호를 생략할 수 있다!
print(type(aa))

my_list = list(aa)
print(my_list)  # []
my_tuple = tuple(my_list)
print(my_tuple)  # ()

# range
# 주로 for문에서 사용
# 같은 데이터를 적은 양의 데이터로 표현 가능 얘는 데이터를 직접 저장하지 않음
my_range = range(10)
print(type(my_range))
print(my_range)
print(my_range[5])
print(my_range[1:4])

my_range = range(1, 10, 3)
print(my_range)
print(my_range)

############################################################################################

# - 4. Mapping ( dictionary )

# Dictionary는 key와 value로 데이터를 저장하는 구조
# { }로 표현
aa = {"name": "홍길동", "age": 40}  # JSON
print(type(aa))  # dict
print(aa["name"])
print(aa.get("age"))  # 불러오는 방법은 두개
aa["address"] = "서울"  # 요소 하나 추가
print(aa)

# dict에서 쓰는 대표적인 method 3개
print(aa.keys())
print(type(aa.keys()))  # 리스트같지만 리스트는 아님
print(list(aa.keys()))  # 이게 list로 바꿔주기
print(aa.values())
print(aa.items())  # 반복할일이 있을 경우 시퀀스화를 위해

##############################################################################################

# - 5. Bool data type => boolean(True, False)

# 사용하는연산자 => and, or, not                 & | '
# 다음의 경우는 python에서 false로 간주함
# 1. 빈 문자열은 false로 간주 => "", ''
# 2. 빈 리스트는 false로 간주 => []
# 3. tuple도 마찬가지 => ()
# 4. dict도 마찬가지 => {}
# 5. 숫자0 false 나머지숫자 true
# 6. None은 false

a=5
b=0
print(a and b)  # 0
print(a & b)  # & : bitwise 연산 # 5 => 0101, 0 => 0000 # 0000 => 0
print(a or b)
print(a | b)  # 0101 | 0000 => 0101 => 5

#########################################################################

# - 6. Set data type
# 집합자료형이고 중복을 허용하지 않는다
# 순서가 존재하지 않음!!

# {} => dict => {"key": "value"}
# {} => set => {1, 2, 3}
my_set = {1, 2, 3, 4, 1, 2}
print(my_set)  # 중복은 알아서 지워줌
my_list = [1, 2, 3, 4, 1, 2]
my_set = set(my_list)  #리스트를 셋으로 바꾸는 방법
print(my_set)

my_str = "Hello"
my_set = set(my_str)
print(my_set)

# set에서 사용하는 연산자
# 합집합(union : |) 교집합(intersection : &) 차집합(difference : -)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2)  # difference

###########################################################################

# -  추가. 날짜관련 사항
# date와 datetime
# 모듈이 필요함

from datetime import date, datetime

today = date.today()
print(today)  # 2020-07-15
# 오늘 날짜는 : 2020년 07월 15일 입니다
my_date = "오늘 날짜는 : {}년 {}월 {}일 입니다"
my_date = my_date.format(today.year, today.month, today.day)  # year month day method 사용
print(my_date)

my_datetime = datetime.today()
print(my_datetime)  # 2020-07-15 10:40:37.919591
print("현재시간은 {}시 {}분 입니다.".format(my_datetime.hour, my_datetime.minute))

# 내일의 날짜는? (달이 바뀌는 상황에서 => 좀 어려움)
# 어제의 날짜는? (오늘이 3월1일이라면? => 윤달 윤년 등등 많이 어려움)
## 그래서 delta가 있음!!
from datetime import date, datetime, timedelta
today = date.today()
days = timedelta(days=-1)
print(today + days)  # 전날
days = timedelta(days=-20)
print(today + days)  # 20일 전

today = datetime.today()
hours = timedelta(hours=-5)
print(today + hours)  # 5시간 전

# 한달전 날짜?
# today = date.today()
# days = timedelta(months=-1)  #months years는 없음
# print(today + days)  # 안됨
# 연도와 달은 새로운 외부 모듈 필요함
# python-dateutil

from dateutil.relativedelta import relativedelta
today = date.today()
months = relativedelta(months=-1)
print(today + months)

# 문자열로 된 특정날짜를 날짜로 변환해서 연산을 하고싶을때는?
from dateutil.parser import parse
my_date = parse("2019-01-30")  # 문자열은 parse로 받음
print(my_date)
my_date = datetime(2019, 1, 30)  # 그냥 숫자는 datetime으로 받기
print(my_date)

################################################################################



# 파이썬 데이터타입 끝~




print('hello world!')