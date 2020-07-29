# Magic function

# -1. 메서드의 이름 앞뒤에 더블언더스코어(__)가 붙어있는
#     메서드를 지칭!! (__init__같은거(생성자))
# -2. class안에 정의되어 있는 특수한 형태의 method
# -3. 특수한 상황에서 그에 맞는 magic function이 호출됨


# class Student(object):
#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept
#         print("{}학과 {} 학생이 생성되었습니다.".format(self.dept, self.name))
#     def __del__(self):
#         print("소멸자 호출")
#
# stu1 = Student("홍길동", "심리")
#
# del stu1  # 객체를 메모리에서 삭제 __del__ 호출해요



a = 100
print(type(a))  # class int가 존재한다

class MyInt(int):
    pass

my_num = MyInt(100)  # class를 상속받아서 인스턴스 만드는 과정

print(my_num + 200)
print(my_num.__add__(200))  # 쌤쌤

#######################################################################

# 매직펑션 사용해보기

class Student(object):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        print("{}학과 {} 학생이 생성되었습니다.".format(self.dept, self.name))
    def __repr__(self):  # 오버라이딩 같은거라고 생각하셈 원래 메모리주소값주는거임
        return  self.name



stu1 = Student("홍길동", "심리")

print(stu1)  # 인스턴스의 class정보와 저장되어 있는 메모리주소가 출력
# __repr__ 을 써서 바꿀수있지

########################################################################

class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def __lt__(self, other):  # 재정의 하는거
        if self.price < other.price:
            return "{}가격이 더 낮아요!!".format(self.model)
        else:
            return "{}가격이 더 높아요!!".format(self.model)
            

car1 = Car("G700", 5000)
car2 = Car("Sonata", 3000)

print(car1.price < car2.price)  # False
print(car1 < car2)  # __lt__ # 이미 정해져있음 내부적으로
# car1이 self, car2가 other에 들어감 # 연산자를 바꿔버림

