# 사용자 지정 예외처리

# BigNumberError 라는 이름의 에러를 만들기 위해 Exception 클래스 상속 받음
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):  # ????
        return self.msg


try:
    print("한 자리 숫자 나누리 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BlockingIOError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError as V_err:
    print(V_err)
    print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BlockingIOError as B_err:
    print(B_err)
    # print("입력값: {0}, {1}".format(num1, num2))
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
