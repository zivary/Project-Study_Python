# 출석번호가 1, 2, 3, 4, 5 였는데
# 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
print("--------------------")
students = [1, 2, 3, 4, 5]
print(students)
print("--------------------")
students = [i+100 for i in students]
print(students)
print("--------------------")

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
print("--------------------")
# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
print("--------------------")