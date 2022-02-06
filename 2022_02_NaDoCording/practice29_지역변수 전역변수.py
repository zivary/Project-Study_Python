gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun을 사용 하겠다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_return(gun, soldiers):  # 경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("--------------------")
print("전채 총 : {0}".format(gun))
print("--------------------")
checkpoint(2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
print("--------------------")
checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))
print("--------------------")
gun = checkpoint_return(gun,2)
print("남은 총 : {0}".format(gun))
