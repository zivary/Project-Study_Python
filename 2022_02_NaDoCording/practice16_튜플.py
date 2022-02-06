# tuple ()
# 리스트와는 다르게 변경이나 추가가 불가능
# 속도는 더 빠르다

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선가스") # 튜플은 update, insert delete 불가능


name = "김종국"
hobby = "코딩"
age = 20
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

