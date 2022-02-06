# __init__ 생성자
# self 를 제외하고 동일한 개수의 값을 넣어줘야 한다.
# marine = Unit("마린") - 에러
# marine = Unit("마린", 40) - 에러

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("--------------------")
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        print("--------------------")


marine = Unit("마린", 40, 5)
marine = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
tank2 = Unit("탱크2", 150, 70)



