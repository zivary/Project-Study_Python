# 메소드 오버로딩
# 자식 클래스에서 정의한 메소드를 사용
# 상속
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage):
#       Unit.__init__(self, name, hp)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 생성, HP: {1}".format(name, hp))
        print("--------------------")

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(
            self.name, location, self.speed))
        print("--------------------")


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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


# class Flyable:
#     def __init__(self, flying_speeed):
#         self.flying_speed = flying_speeed

#     def fly(self, name, location):
#         print("[공중 유닛 이동]")
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
#             name, location, self.flying_speed))
#         print("--------------------")


# class FlyableAttackUnit(AttackUnit, Flyable):
class FlyableAttackUnit(AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed = 0 처리
        # Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(
            self.name, location, self.speed))
        print("--------------------")


# 벌처: 지상 유닛, 기동성이 좋음
vultyre = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중 요닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 50, 3)

# Unit클래스의 move 메소드를 AttackUnit 클래스가 상속받아 사용
vultyre.move("11시")
print("--------------------")
# Flyable 클래스의 fly 메소드를 FlyableAttackUnit 클래스가 상속받아 사용
# battlecruiser.fly(battlecruiser.name, "9시")
print("--------------------")
# Unit클래스의 move 메소드를 상속받은 AttackUnit 클래스를 상속받은 
# FlyableAttackUnit 클래스에서 move 메소드를 재정의(오버로딩)하여 사용
battlecruiser.move("11시")
print("--------------------")
