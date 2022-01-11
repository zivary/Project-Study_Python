#묘듈 사용

import practice50_모듈
practice50_모듈.price(3) # 3명이서 영화 보러 걌을 때 가격
practice50_모듈.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
practice50_모듈.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 

import practice50_모듈 as mv
mv.price(6)
mv.price_morning(7)
mv.price_soldier(8)

from practice50_모듈 import *
price(9)
price_morning(10)
price_soldier(11)

from practice50_모듈 import price, price_morning
price(12)
price_morning(13)
price_soldier(14)  # 에러 발생

from practice50_모듈 import price_soldier as price
price(15)  # 군인 할인 가격이 나옴
