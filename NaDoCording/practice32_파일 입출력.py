# "w" = write 쓰기 용도
# score_file = open("score.txt", "w", encoding="utf=8")
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()


# "a" = append 이어서 쓰기
# score_file = open("score.txt", "a", encoding="utf=8")
# score_file.write("과학: 80\n")
# score_file.write("코딩: 100\n")
# score_file.close()

# "r" = read 쓰기 용도
# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.read())
# score_file.close()

# 한 줄씩 불러오기
# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 문서가 총 몇줄인지 모르는 경우
score_file = open("score.txt", "r", encoding="utf=8")
while True:
    line = score_file.readline()
    if not line:  # 만약 라인에 내용이 없다면
        break
    print(line, end="")
score_file.close()

print("--------------------")

# list에 넣어서 출력
score_file = open("score.txt", "r", encoding="utf=8")
lines =score_file.readlines() # 한 줄 쌕 list 형태로 저장
print(lines)

print("--------------------")

for line in lines:
    print(line, end="")
score_file.close()
print("--------------------")
