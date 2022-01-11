# 마린: 공경 유닛, 군인. 총을 쏠 수 있음
print("--------------------")
name = "마린" #유짓의 이름
hp = 40 # 유닛의 체력
damage = 5 #유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}".format(hp, damage))
print("--------------------")

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
print("--------------------")
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))
print("--------------------")
tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 70

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}".format(tank2_hp, tank2_damage))
print("--------------------")

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
print("--------------------")
attack(name, "1시", damage)
print("--------------------")
attack(tank_name, "1시", tank_damage)
print("--------------------")
attack(tank2_name, "1시", tank2_damage)
print("--------------------")
