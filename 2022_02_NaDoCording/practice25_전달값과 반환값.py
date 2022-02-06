# 함수 def
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("{0}원 입금이 완료되었습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:  # 출금액이 잔액보다 많으면
        print("{0}원 출금이 완료되었습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    if balance >= money + commission:  # 출금액이 잔액보다 많으면
        print("{0}원 출금이 완료되었습니다. 수수료는 {1}원, 잔액은 {2}원입니다.".format(
            money, commission, balance - (money + commission)))
        return commission, balance - (money + commission)
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return commission, balance  # tuple 형식 반환


print("--------------------")
balance = 0  # 처음 잔액
balance = deposit(balance, 10000)
print("총 잔액은 " + str(balance) + "원 입니다.")
print("--------------------")
balance = withdraw(balance, 2000)
print("총 잔액은 " + str(balance) + "원 입니다.")
print("--------------------")
balance = withdraw(balance, 50000)
print("총 잔액은 " + str(balance) + "원 입니다.")
print("--------------------")
commision, balance = withdraw_night(balance, 900)
# print("수수료 {0} 원이며, 잔액인 {1} 원입니다.".format(commision, balance))
print("총 잔액은 " + str(balance) + "원 입니다.")
print("--------------------")
