absent = [2, 5]  # 결석
no_book = [7]  # 책을 깜빡함
print("--------------------")
for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    print("{}님 책을 읽어주세요.".format(student))
    print("--------------------")
    if student in absent:
        print("{}님 오늘 안 오셨어요? 그럼 다음!".format(student))
        print("--------------------")
        continue
    elif student in no_book:
        print("책을 안 가지고 온 분이 있네요?\n오늘 수업은 여기까지. \n{}은 교무실로 따라와.".format(student))
        print("--------------------")
        break
