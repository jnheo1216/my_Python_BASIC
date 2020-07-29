# python의 입출력
# 입력을 받고 싶을 때?
# console입력을 받으려면 input
my_input = 1  # input("입력값을 넣으세요!! : ")
print(type(my_input))
print(my_input)

# 기본적으로 print함수는 한줄을 출력하고 line feed(줄바꿈)을 수행
# 그게 싫으면?
print(type(my_input), end=" ")
print(my_input)
print()

#######################################################################

# Control Statement (제어문)

# - 1. if문
# python의 조건문은 두가지 방식
# 전통적인 if elif else

a= 15
if a % 3 == 0:
    print("3의배수임")
elif a % 5 == 0:
    print("5의배수임")
elif a % 127 == 0:
    pass  # 이거 넣어주지 않으면 문법 에러남
else:
    print("3, 5 둘다아님")

print()
# in을 이용한 구문
my_list = ["서울", "인천", "부산"]
if "수원" in my_list:
    print("수원 in my_list")
else:
    print("수원 없음")

print()
##################################################################

# - 2. for문
# 두가지 형태가 있음
# for ~ in range() => 반복횟수를 지정할 경우
# for ~ in list, tuple, dict ... => 가지고 있는 데이터만큼 반복할 경우

# 1부터 100까지 합
my_sum = 0
for tmp in range(1, 101, 1):
    my_sum += tmp
print("누적값은 : {}".format(my_sum))

# 집합자료형을 이용해서 for문
my_list = ["서울", "인천", "부산"]
for tmp in my_list:
    print(tmp)

# tuple관련 예
my_data = [(1, 2), (3, 4), (5, 6)]
total = 0
for (tmp1, tmp2) in my_data:
    total += (tmp1 + tmp2)  #tuple이 나오면? for에서 받는걸 tuple로 받으면 됨
print(total)

########################################################################

# python에는 특이하게 list comprehension 이라는 기능이 있음!!
# 하나의 자료형으로 다른 list를 쉽게 생성하는 방법 중 하나

my_list = [1, 2, 3, 4, 5]
goal = [2, 4, 6, 8, 10]
my_goal = []
for tmp in my_list:
    my_goal.append(tmp*2)
print(my_goal)
print(goal)

# 다른 방법
my_list = [1, 2, 3, 4, 5]
goal = [2, 4, 6, 8, 10]
my_goal = [tmp * 2 for tmp in my_list]  # 아주 간단하게 가능
print(my_goal)
print(goal)

# 짝수만 뽑아보자
my_list = [1, 2, 3, 4, 5]
my_goal = [tmp for tmp in my_list if tmp % 2 == 0]
print(my_goal)

###########################################################################

#  - 3. while문

idx = 0
while idx < 10:
    print("현재 idx의 값은 : {}".format(idx))
    idx += 1  # idx++은 문법에러 남

########################################################################





