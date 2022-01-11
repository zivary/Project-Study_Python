# pass
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 생성, HP: {1}".format(name, hp))
        print("--------------------")


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass  # 일단은 그냥 넘어간다


# 서플라이 디폿: 건물, 1개 건물 = 8 유닛 생성 가능.
supply_depot = BuildingUnit("서플라이 디폿", 500, "본진")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass
    print("[알림] 게임을 종료합니다.")
    

game_start()
game_over()
