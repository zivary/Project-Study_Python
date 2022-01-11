# Quiz) 당신의 학교에서 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤틀르 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 총해 1명은 치킨, 3명은 커피 쿠폰을 답게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당참자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # lst 의 요소를 무작위로 섞는다.
# print(lst)
# print(sample(lst,1)) # lst 중 1개를 무작위로 뽑는다.

# (정답)
from random import *
print("--------------------")

users = range(1, 21)  # 1 부터 21 직전까지 숫자를 생성
print(users)
print(type(users))  # range 타입으로 만들어져서 list 타입의 명령을 사용할 수 없음

print("--------------------")

# list 타입의 명령어인 sample을 사용하였음으로 range 타입에서 list 타입으로 장동 변환
winner = sample(users, 1)
print(winner)
print(type(winner))

print("--------------------")

users = list(users)  # users을 list타입으로 바꿔줌
print(users)
print(type(users))

print("--------------------")

shuffle(users)  # shuffle 명령어는 list 타입에서 사용하는 명령어 입으로 형 변환 후 사용 가능(?)
print(users)
print(type(users))


print("--------------------")

winners = sample(users, 4)  # 당첨자 4명을 뽑아서 치킨 1명, 3명은 커피
print(winners)
print(type(winners))  # list 에서 sample을 뽑았음으로 결과도 sample 타입?
print("--------------------")

print(" -- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

print("--------------------")
