
# while
print("--------------------")

customer = "토르"
index = 5
while index >=1:
    print("{0}님 커피가 준비 되었습니다. 주문이 {1}개 남았습니다.".format(customer,index))
    index -= 1
    if index == 0:
        print("주문이 모두 완료되었습니다.")

print("--------------------")  

customer = "아이언맨"
index = 1
while True:
    print("{0}님 커피가 준비 되었습니다. 호출{1} 회".format(customer,index))
    index += 1
    if index == 11:
        print("커피를 패기합니다.")
        break

print("--------------------")

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    if person == customer:
        print("감사합니다.")
        break