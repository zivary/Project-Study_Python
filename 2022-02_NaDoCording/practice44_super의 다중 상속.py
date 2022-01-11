# super의 다중 상속
# super() 생성자로 부모 클래스를 상속 받을 경우 가장 먼저 상속받은 클래스만 상속된다
print("--------------------")
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")

print("--------------------")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 드랍쉽 생성
dropship = FlyableUnit() # Unit 생성자 만 생성

print("--------------------")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

# 드랍쉽 생성
dropship = FlyableUnit() # Flyable 생성자 만 생성

print("--------------------")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)
        
# 드랍쉽 생성
dropship = FlyableUnit() # Unit, Flyable 생성자 모두 생성

print("--------------------")
