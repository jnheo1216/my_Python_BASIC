# 1990년 이전
# 가장 대표적인 프로그램 작성방식으로
# 구조적 프로그래밍 (절차적프로그래밍)
# '기능'으로 세분화해서 각각의 기능을 모듈로 제작 프로그램을 작성
# 장점 : 설계가 쉬움 => 빨리 만듬 => 이득
# 프로그래밍 하기 쉬움
# 단점 : 수정, 유지보수가 어려움 구조적프로그래밍특

# 세상이 변하고 프로그램의 유지보슈가 중요하게됨

# 현실세계의 해결해야하는 문제에 대한 구성요소를 파악
# 객체(object)
# => Object Oriented Programming (OOP)
# 개체들을 파악해서 그 개체들의 관계를 프로그래밍하는 방식을
# => 객체지향프로그래밍이라 한다

# 개체들을 파악한 후 이 각각의 개체를 프로그램적으로 묘사해야해요
# => 객체 모델링

# 예) 사람을 프로그램적으로 묘사해보자
# 추상화(Abstraction) 과정을 거쳐서 객체모델링을 해보자
# 이런 개체들은 속성, 행위가 있다!!
#             변수(property, member field, field),
#             함수(method)
# class를 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게되요!!
# class => 1. 객체모델링의 수단

# class 사람
#       키(변수) h => float
#       몸무게 (변수) w => float
#       나이 (변수) a => int
#       이름 (변수) n => str
#       걷는다 (메소드)
#       말한다 (메소드)
#       잔다 (메소드)

# class는 data type의 관점에서 봤을 때는 기존 데이터타입을 이용해서
# 새로운 data type을 만드는 것이라소 볼 수 있어요
# calss => 추상적인 데이터 타입이라 불려요! (Abstract data type)
#       => ADT

#########################################################################

# 구조적 프로그래밍
# 프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈화
# 프로그램 구조를 이해하기 쉽고 프로그램을 빠르게 만둘 수 있음
# 프로그램 규모가 커지면 유지보수와 코드의 재사용에 한계가 온다.

# 객체지향 프로그래밍
# 현실세계의 해결해야 하는 문제를 그대로 프로그램으로 묘사
# 프로그램을 구성하는 주체를  파악하고
# 그 객체들간의 데이터 효율에 초점을 맞추어서 프로그램을 생성
# 설계하고 구성하는데 상대적으로 어려워
# 제대로 작성한 객체지향 프로그래밍은 유지보수와 재사용성에 상당한 이점

#########################################################################

# 학생의 이름, 학과, 학번, 평점을 저장하는 방법

stu_name = "홍길동"
stu_dept = "심리학과"
stu_num = "20201134"  # 문자열이 뭐 하기 편하대
stu_grade = 3.5

# 만약 4명의 학생이 있으면?

stu1_name = "김길동"
stu1_dept = "컴공학과"
stu1_num = "20201135"
stu1_grade = 3.8

# 좀 난잡해 너무 쓸데없이 반복적이고 확장성도 없음

stu_name = ["홍길동", "김길동", "신사임당"]
stu_dept = ["심리학과", "컴퓨터", "경영"]
stu_num = ["20201134", "20201135", "20201138"]
stu_grade = [3.5, 2.0, 4.0]

# index를 이용해 처리하는게 쉽진 않아
# 코드에 모든의미가 다 내포되어있는게 아닌 문제가 발생

# 어떻게 하면 객체지향적으로 표현할까?
# 학생이라는 개념을 프로그램적으로 모델링 해보자


class Student(object):
    def __init__(self, name, dept, num, grade):  # 이게 함수요 # 클래스는 무조건 맨앞에 이거 정해져있음 # 공간에 대한 초기화 # init는 일반적으로 데이타 받는게 좋음
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade  # 이 4개의 변수같은걸 instance variable

# 클래스에 데이터를 직접 저장하는게 아니라
# 클래스를 기반으로 'instance(객체object)'라는 메모리 공간 확보
# self : 그 객체의 주소, 객체 그 자체를 의미함

students = []
students.append(Student("홍길동", "심리학과", "20201134", 3.5))
students.append(Student("김길동", "컴공학과", "20201135", 2.5))
students.append(Student("신길동", "경영학과", "20201138", 4.0))

print(type(students[1]))
print(students[1].dept)

########################################################################

## python은 객체지향언어
## 파이썬에서 나오는 모든 것은 다 객체(instance)에요

a = 10
print(type(a))  #  <class 'int'>
my_list = [10]
print(type(my_list))  # <class 'list'>

# list나 int의 class가 있구나 하는 걸 알 수 있다

# 숫자도 객체고 문자열도 객체고 심지어 함수까지 객체였던거임 ㄷㄷ
# 객체(instance)가 있다는 건 => class가 존재한다는 것
# 객체(instance) => 변수, method

# 객체(instance)란 속성과 같은 여러가지 데이터 + 메소드를 가지고있는
# 데이터구조를 지칭


class Student2(object):
    def __init__(self, name, dept, num, grade):  # constructor(생성자) # initializer
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade
    def __repr__(self):  # 이걸 안하면  프린트하면 메모리값을 줌
        return self.name  # 이젠 name에 들어있는 것을 줌
    def change_dept(self, tmp_dept):
        # tmp_dept가 정상적인 학과인지 확인하는 코드
        self.dept = tmp_dept

stud = Student2("길동", "심리학과", "20201134", 3.5)
stud.dept = "경영"  # 이건 다이렉트로 접근하는 법 # 권장하지 않음 # method를 통하는 게 원칙
# information hiding
stud.change_dept("경영학")  # 변수에 직접 접근 안하고 method로 접근하는 법 # 이렇게해야함
print(stud.dept)

###############################################################################

# python이 제공하는 특수한 내장함수들 
# dir()
# 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려줌
print(dir(stud))

stud.depts = "철학과"  # 철자 틀린 것도 허용해줌 ㄷㄷ # 새로운거 추가해준다고 만들어줌
print(dir(stud))

# python의 함수도 객체
def myfunc(a, b):
    return a + b
print(dir(myfunc))
myfunc.my_name = "홍길동"  # 이것도 가능함 ㄷㄷ
print(dir(myfunc))

class Student3(object):
    scholarship_rate = 3.0  # class variable
    def __init__(self, name, dept, num, grade):  # constructor(생성자) # initializer
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade
    def __repr__(self):  # 이걸 안하면  프린트하면 메모리값을 줌
        return self.name  # 이젠 name에 들어있는 것을 줌
    def is_scholarship(self):
        if self.grade > Student3.scholarship_rate:
            print("합격!")
            return True
        else:
            print("불합격")
            return False

studyy = Student3("길동", "심리학과", "20201134", 3.5)
studyy.is_scholarship()
print(studyy)

#########################################################################

# namespace (네임스페이스)
# 객체들이 가지는 데이터를 나누어서 관리하는 공간을 지칭
# instance namespace
# class namespace
# superclass namespace
# instance < class < superclass : 포함관계
# 위에거를 예로 하면, scholaship_rate는 class namespace고
#                  name, grade 등등은 instance namespace임

# python은 동적으로 속성이나 method를 추가할 수 있어요
studyy.scholarship_rate = 4.5  # 이거 됨?? class namespace에 있는건데?
# : 된다. 근데 좀 다르게 된다
#   현재 있는 class namespace에 있는 걸 건드리진 못하고
#   instance namespace에 또 하나 만들어서 저장함
#   그래서 클래스변수 앞에는 정확히 클래스 이름을 적어주는게 좋음

# instance method(self인자를 가지고 있는 method)는 하나의
# 인스턴스에 한정된 데이터를 생성, 변경, 참조하기 위해서 사용되요!

# class method는 클래스를 인자로 받아서 class variable을
# 생성, 변경, 참조하기 위해 사용되요 @classmethod


class Student4(object):
    scholarship_rate = 3.0  # class variable
    def __init__(self, name, dept, num, grade):  # constructor(생성자) # initializer
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade
    def __repr__(self):  # 이걸 안하면  프린트하면 메모리값을 줌
        return self.name  # 이젠 name에 들어있는 것을 줌
    def is_scholarship(self):
        if self.grade > Student3.scholarship_rate:
            print("합격!")
            return True
        else:
            print("불합격")
            return False
    @classmethod  # 이걸로 밑의 메소드가 클래스메소드인걸 명시해줘야함!!
    def chan_scholaship(cls, rate):  # self가 아니고 cls를 넣음 # 클래스메소드
        cls.scholarship_rate = rate
        print("장학금기준 바뀜")
    @staticmethod
    def is_valid_scholaship(rate):  # self나 cls 안받음 ㄷㄷ
        if rate < 0:
            print("아니 어떻게 학점이 음수야")

stud4 = Student4("길동홍", "심리학과", "20201134", 3.5)
Student4.chan_scholaship(3.7)  # 클래스 메소드 사용

# static method : 일반함순데 클래스안에서 작동함! @staticmethod

########################################################################

# information hiding (정보은닉)
# instance가 가지는 속성은 매우매우 중요한 데이터이기때문에
# 외부에서 직접적으로 access하는건 좋지 않아요!

# 어떻게 막지?
# 언어마다 다름
# ex) JAVA => access modifier(접근제어자)
#             public vs private

# 파이썬은 어떻게할까?
class Student5(object):
    scholarship_rate = 3.0  # class variable
    def __init__(self, name, dept, num, grade):  # constructor(생성자) # initializer
        self.name = name
        self.__dept = dept  # 언더바를 두개 붙여주면 된다
        self.num = num
        self.grade = grade
    # private 처리가 된 속성이 있으면 외부에서 직접 못건드려
    # access가 안되기 때문에 method를 이용해서 사용하도록 처리해야함
    # private로 되어있는 속성의 값을 알아오는 용도의 method가 필요
    # => getter (getter는 이름이 정해져있음)
    def getDept(self):
        return self.__dept
    # => setter는 값을 설정해주는 method
    def set_dept(self, dept):
        self.__dept = dept
    def __print_date(self):  # 프라이빗메소드 # 메소드도 클래스 바깥의 접근을 막을 수 있음
        return self.name

stud5 = Student5("길동홍", "국문학과", "20201134", 3.5)
# print(stud5.dept)  # 의미없음 왜냐? 언더바 두개를 붙여서 정보은닉을 했으니까
print(stud5.getDept())

# 여기까지가 단일class에 대한 이론적인 내용

##########################################################################

# 객체지향을 하는 이유 => 유지보수와 재사용성
# 재사용성을 위한 대표적인 객체지향 기법 => Inheritance(상속)
# 객체지향의 꽃 # 객체지향 특)

# 두개의 클래스를 이용해서 상속을 알아보자
# Unit class, Marin class
# Unit class : 모든 유닛이 공통으로 가지고 있는 속성과 method로 구성
#              super class로 사용, base class
# Marin => sub class

# class object():
#       ~
#       ~
# python의 모든 클래스는 object class!
# 파이썬의 모든 클래스는 object class를 상속해야해!!

class Unit(object):  # 괄호의 의미 : 상속의 의미
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__  # 네놈의 클래스 이름을 찾아가겠다
        self.damage = damage
        self.life = life
    def show_status(self):
        print("직업 : {}".format(self.utype))
        print("공격력 : {}".format(self.damage))
        print("체력 : {}".format(self.life))

class Marin(Unit):
    def __init__(self, damage, life, range_up):
        super(Marin, self).__init__(damage, life)  # 상위클래스의 인자들을 받아오는 법
        self.range_up = range_up  # 내가 필요로 하는거만 추가하면 된다
    def show_status(self):  # method overizing(메서드 재정의) # 이럴거면 왜 상속함?
        super(Marin, self).show_status()  # 이게 상속이지
        print("사업 유무 : {}".format(self.range_up))

class Zelot(Unit):
    pass

marin_1 = Marin("100", "100", True)
marin_1.show_status()

zelot_1 = Zelot("100", "100")
zelot_1.show_status()

#######################################################################

# 사용할 유닛들은 마린, 벌쳐, 메딕, 드랍쉽

class Unit1(object):
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life
    def show_status(self):
        print("직업 : {}".format(self.utype))
        print("공격력 : {}".format(self.damage))
        print("체력 : {}".format(self.life))
    def attack(self):
        pass

class Marin1(Unit1):
    def __init__(self, damage, life, range_up):
        super(Marin1, self).__init__(damage, life)
        self.range_up = range_up
    def show_status(self):  # overriding
        super(Marin1, self).show_status()
        print("사업 유무 : {}".format(self.range_up))
    def attack(self):  # overriding
        print("마린이 공격함! 땅땅땅빵")
    def stimpack(self):
        if self.life < 20:
            print("스팀팩못씀")
        else:
            self.life -= 10
            self.damage *= 1.5
            print("마린이 스팀팩 씀 ㄷㄷ")

class Medic1(Unit1):
    def attack(self):
        print("메딕이 치료함다")

class Vulture1(Unit1):
    def __init__(self, damage, life, amount_of_mine):
        super(Vulture1, self).__init__(damage, life)
        self.amount_of_mine = amount_of_mine
    def attack(self):  # overriding
        print("벌처가 공격함! 퉁퉁퉁")

class Dropship1(Unit1):
    def attack(self):
        print("특정위치로 이동함 슈슈슈슝")
    def board(self, unit_list):
        self.unit_list = unit_list
        print("태웠다")
    def drop(self):
        print("내렸다")
        return self.unit_list

marin1 = Marin1("100", "100", False)
marin2 = Marin1("100", "100", False)
marin3 = Marin1("100", "100", False)

medic1 = Medic1("0", "100")

vulture1 = Vulture1("100", "100", 3)
vulture2 = Vulture1("100", "100", 3)

# 하나로 묶기
troop = list()
troop.append(marin1)
troop.append(marin2)
troop.append(marin3)
troop.append(medic1)
troop.append(vulture1)
troop.append(vulture2)

dropship = Dropship1("0", "100")

# 드랍쉽에 태우기
dropship.board(troop)

# 가자
dropship.attack()

# 내려
my_list = dropship.drop()

# 돌격
# for unit in my_list:
#     if isinstance(unit, Marin1):
#         unit.stimpack()

#######################################################################

# 각 사람에 대한 데이터를 읽어서 성적순으로 출력
# 1등 누구누구 몇점
from operator import itemgetter


class Take_stu(object):
    def __init__(self, stu_list):  # constructor(생성자) # initializer
        self.__name = stu_list[0]
        self.__fst = stu_list[1]
        self.__scd = stu_list[2]
        self.__trd = stu_list[3]
        self.avg = round((int(stu_list[1]) + int(stu_list[2]) + int(stu_list[3])) / 3, 1)
    def __repr__(self):  # 이걸 안하면  프린트하면 메모리값을 줌
        return "{} {}".format(self.__name, self.avg)


def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 띄어쓰기를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기

def take_avg(name_list):
    avg = (int(name_list[1]) + int(name_list[2]) + int(name_list[3])) / 3
    return round(avg, 1)  # 반올림

file2 = my_read_txt('student_score.txt')

n = 0
for m in file2:
    l = take_avg(m)
    file2[n].append(l)
    n += 1

sort_arry = []
for name in sorted(file2, key=itemgetter(4)):  # 이거하나면 정렬 개쉬움
    sort_arry.append(name)

sort_arry.reverse()
print()
print()

k = 1
for j in sort_arry:
    print("{} 학생 ".format(j[0]), "{}등 ".format(k), "{}점".format(j[4]))
    k += 1

# students는 학생데이터가 들은 배열. 내꺼에서는 file2
# result = sorted(students, key=lambda stu: stu.avg)



