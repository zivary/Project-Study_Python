# with

import pickle
# profile.pickle 을 읽기 전용으로 열고 profile_file 변수에 담음
# with 문은 pickle 문을 답아줄 필요 없이 with 문을 나오면서 pickle 파일이 저절로 닫힌다.
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# 위랑 같은 의미의 명령문
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # 파일의 형태(내용)을 데이터로 profile에다 담아 가지고 옴
# print(profile)
# profile_file.close()

# pickle을 사용하지 않고 일반 파일을 읽어오고 쓰는 것을 with 문으로 해보자!
# 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.\n")

# 이어서 쓰기
with open("study.txt", "a", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요._2\n")
with open("study.txt", "a", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요._3\n")

# 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
