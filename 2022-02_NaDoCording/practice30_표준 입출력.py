# sep 콤마(,) 자리에 무엇이 들어갈 것 (기본값은 " ")
import sys
print("python", "Java", sep=", ")
print("python", "Java", "JavaSrcipt", sep=" vs ")

print("--------------------")

# end: 문장의 끝 부분에 "?" 를 넣어주고 다음을 이어서 출력한다.
print("python", "Java", sep=", ", end=" ? ")
print("무엇이 더 재미있을까요?")

print("--------------------")

# ?????
print("python", "Java", file=sys.stdout)  # 표준 출력으로 처리
print("python", "Java", file=sys.stderr)  # 표준 에러로 처리

print("--------------------")

# 시험 성정 표기
print("--------------------")
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject, score)

print("--------------------")

for subject, score in scores.items():
    # *.ljust(6) - 총 6칸을 확보하고 왼쪽 정렬
    # *.rjust(4) - 총 4칸을 확보하고 오른쪽 정렬
    print(subject.ljust(6), str(score).rjust(4), sep=":")

print("--------------------")

# 은행 대기순번표
# 001 002, 003, 004, ,,,
# *.zfill(3) - 총 3칸을 확보하고 빈 칸은 0으로 채움
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

print("--------------------")

# 표준 입력 input
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자에게 입력 받은 값은 항상 String 
print("입력하신 값은 " + answer + "입니다.")

print("--------------------")
