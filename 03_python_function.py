# python 함수
# 2가지가 있다
# 1. 내장함수
# 2. 사용자정의함수 (user define function)

# 함수 => 특정 작업을 수행하는 일정량의 코드 모음
# 함수를 만드려면 어떻게?



def my_sum(a, b, c):
    return a + b + c

#함수는 위에 두줄 반드시 띄워서 써야함 (관습)

result = my_sum(10, 20, 30)
print(result)

# 함수를 호출하는데 전달되는 인자의 수가 가변적일때는 어쩌나요?? 답은 '튜플'이다.


def my_sum2(*args):
    tmp = 0
    for k in args:
        tmp += k
    return  tmp

result = my_sum2(1, 2, 3, 4)
print(result)

# python은 함수의 결과값이(리턴값)이 2개이상일수있음


def my_operator(a, b):
    result1 = a + b
    result2 = a - b
    return (result1, result2)  #튜플로 리턴함 # 보통 괄호는 생략을 함
# 결국 2개이상리턴이 아니라 튜플 하나 리턴한다는 소리
tmp1, tmp2 = my_operator(10, 20)
print(tmp1)
print(tmp2)

# 함수에서 default parameter를 사용해보자


def my_default(a, b, c=True):  #가변인자(formal parameter) #무조건 마지막 값만 가능해요!!
    data = a + b
    if data > 10 and c:
        return data
    else:
        return 0
# 만약 2개만 받으면 저기 c를 쓸 수 있다는 뜻 #3개받으면 그냥 하는거고
result1 = my_default(10, 20, False)
result2 = my_default(10, 20)  # 실인자(real parameter)

print()
# python함수의 인자는 mutable, immutable 둘중의 하나
# call-by-value & call-by-reference
# python의 함수에 인자를 전달하고 받아요!!
# 어떤 경우는 실인자의 데이터가 변하는 경우가 있어요
# 어떤 경우는 실인자의 데이터가 변하지않는 경우가 있어요


def my_func(tmp_number, tmp_list):
    tmp_number = tmp_number + 100
    tmp_list.append(100)

data_x = 10  # Numeric
data_list = [10]  #list

my_func(data_x, data_list)
print(data_x)  #리턴이 없어서 함수를 돌아도 출력값은 똑같다. # immutable(ex. 숫자 문자열 튜플)
print(data_list)  # 함수안에서 변하고 왔으니까 출력이 바뀜 # mutable(ex. list dict)

##########################################################################

# 내장함수
# 어어어어어어어엄청 많음

# id() 함수는 좀 알아둘 필요가 있음
# id() : 객체의 고유 주소값을 return하는 함수
my_list1 = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]
print(id(my_list1))
print(id(my_list2))

my_num1 = 100
my_num2 = 100
print(id(my_num1))
print(id(my_num2))
# 0~256 까지의 숫자는 너무나 많이 쓰기 때문에 객체의 주소를 이미 지정해놓음
# 성능을 위한 하나의 예외 # 파이참은 더 많은 숫자에 적용함

# 내장함수는 너무 많고 중요하지만
# 일반적으로 코드를 작성해 나가면서 하나씩 알아가는 방법이 좋아연

# 함수와는 다르지만 함수의 역할을 수행하는 lambda expression(람다표현식)
# lambda
# 한줄로 함수를 정의하는 방법
# 함수의 이름이 없어?!(anonymous function)
# 이름이 없기 때문에 변수에 저장 # 함수의 인자로 사용
# 함수의 결과값(리턴값)으로 함수를 리턴
# => first class
my_lambda = lambda x1, x2, x3: x1 + x2 + x3
# 괄호안써도된다 # return따위 안씀
print(my_lambda(10, 20, 30))   # => 10 + 20 + 30
# 결정적으로 람다와 함수가 다른 점은, 람다는 대체식이에요!!



