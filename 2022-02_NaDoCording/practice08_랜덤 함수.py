
from random import *
print("--------------------")
# 0.0 <= 난수 < 1.0 인 임의의 값 생성
print(random())
print("--------------------")
# 0.0 < 난수 < 10.0 인 임의의 값 생성
print(random() * 10)

print("--------------------")
# 실수형을 정수형으로 형변환
print(int(random() * 10)) # 0 이상 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print("--------------------")
print(int(random() * 10)+1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random() * 10)+1)
print(int(random() * 10)+1)
print(int(random() * 10)+1)
print(int(random() * 10)+1)
print("--------------------")
print("로또 번호 생성_1")
print(int(random() *45)+1) # 1 이상 ~45 이하의 임의의 정수 값 생성
print(int(random() *45)+1)
print(int(random() *45)+1)
print(int(random() *45)+1)
print(int(random() *45)+1)
print(int(random() *45)+1)
print("--------------------")
print("로또 번호 생성_2")
print(randrange(1,46)) # 1 이상 ~ 46 미민의 임의의 정수 값 생성
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print("--------------------")
print("로또 번호 생성_3")
print(randint(1,45)) # 1 이상 ~ 45 이하의 임의의 정수 값 생성
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print("--------------------")