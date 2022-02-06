# 다중 상속
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage):
#       Unit.__init__(self, name, hp)

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} 생성, HP: {1}".format(name, hp))
        print("--------------------")


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        print("{0} 생성, HP: {1}, 공경력: {2}".format(name, hp, damage))
        print("--------------------")

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
            self.name, location, self.damage))
        print("--------------------")

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))
        print("--------------------")


# 드랍쉽:  공중 유닛, 수송기. 유닛을 수송. 공경X
# 날 수 있는 기능을 가진 클래스


class Flyable:
    def __init__(self, flying_speeed):
        self.flying_speed = flying_speeed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))
        print("--------------------")
        


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 밣사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.attack("6시")
valkyrie.damaged(150)
valkyrie.damaged(150)
print(valkyrie.hp)