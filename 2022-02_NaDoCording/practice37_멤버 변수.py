# 멤버 변수
# self.name = name
# self.hp = hp
# self.damage = damage

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("--------------------")
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 레이스: 공중 유닛, 비행기.
wraith1 = Unit("레이스", 80, 5)

# clocking 멤버 변수 추가(clockong 개발)
wraith2 = Unit("레이스2", 80, 5)

wraith2.clocking = True  # wraith2 에 클로킹 스킬을 업그래이드
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
    
class Unit2:  # clocking 이 개발된 유닛
    def __init__(self, name, hp, damage, clocking):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.clocking = clocking
        print("--------------------")
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        if self.clocking == True:
            print("{0} 는 현재 클로킹 상태입니다.".format(self.name))


wraith3 = Unit2("클로킹 중인 레이스", 80, 5, True)
wraith4 = Unit2("마나가 없는 레이스", 80, 5, False)
# wraith5 = Unit2("클래킹 개발이 안된 레이스", 80,5) #error
