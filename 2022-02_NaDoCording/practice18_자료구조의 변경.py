# 자료구조의 변경

menu = ("커피", "우유", "주스")
print(menu, type(menu)) # menu와 그 타입 보기

menu = set(menu) # set 타입에서 list 타입으로 타입 변환
print(menu, type(menu)) # menu와 그 타입 보기

menu = list(menu) # set 타입에서 list 타입으로 타입 변환
print(menu, type(menu)) # menu와 그 타입 보기

menu = tuple(menu) # set 타입에서 list 타입으로 타입 변환
print(menu, type(menu)) # menu와 그 타입 보기
