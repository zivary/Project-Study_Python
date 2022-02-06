# dictionary

from typing import ChainMap
print("--------------------")
# 정수형 변수 사용
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print("--------------------")
print(cabinet.get(3))
print(cabinet.get(100))
print("--------------------")

# 중목되면 최근에 입력된 값으로 변수 저장
cabinet = {3: "유재석", 100: "김태호", 100: "박명수"}
print(cabinet[3])
print(cabinet[100])
print("--------------------")
print(cabinet.get(3))
print(cabinet.get(100))
print("--------------------")

# print(cabinet[5]) # 값이 없으면 에러를 발생시키고 종료
# print("Hi") # 위에서 종료되어 값이 출력되지 않음
print(cabinet.get(5))  # 값이 없다면 None을 출력함
print(cabinet.get(5, "Default"))  # 값이 없다면 초기값 출력 옵션
print("Hi")
print("--------------------")
print(3 in cabinet)  # True  - 3 라는 키를 cabinet 에 있는가?
print(5 in cabinet)  # False - 5 라는 키를 cabinet 에 있는가?
print("--------------------")

# 문자열 변수 사용
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print("--------------------")
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # cabimet update
cabinet["C-20"] = "조세호"  # cabinet insert
print(cabinet)
print("--------------------")
# 간 손님
del cabinet["A-3"]  # cabinet delete
print(cabinet)
print("--------------------")
# key 값 들만 출력
print(cabinet.keys())
print("--------------------")
# value 들만 출력
print(cabinet.values())
print("--------------------")
# key, value 쌍으로 출력
print(cabinet.items())
print(cabinet)
print("--------------------")
# 목욕탕 폐점
cabinet.clear()
print(cabinet)


