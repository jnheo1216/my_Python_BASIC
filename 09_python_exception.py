
# exception (예외)
# Error - compile time error : 문법오류
# Error - runtime error : 실행 시 발생하는 오류

# 어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로
# 수행시킬 수 있는 방법이 있어요


# try~
# except
# else
# finally

def my_func(my_list):
    total_sum = 0  
    
    try:
        total_sum = my_list[0] + my_list[1] + my_list[2]
    except Exception:
        print("오류가 존재합니다.")  # 예외처리를 해야 함
    else:
        print("오류가 없네여")
    finally:
        print("무조건 수행")


my_func([1,2])










