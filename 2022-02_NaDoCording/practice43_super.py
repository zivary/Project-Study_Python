## super
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
        # Unit.__init__(self, name, hp, 0)
        # 대신 super().__init__(name, hp, 0) 사용
        # super 뒤에 () 를 넣어주고 self 매개변수을 빼준다.
        super().__init__(name, hp, 0)
        self.location = location

