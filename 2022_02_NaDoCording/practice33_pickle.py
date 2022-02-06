# pickle 사용하기
# 데이터를 pickle이라는 확장자 파일로 저장했다가 불러오기

import pickle
# "wb" Write Binary pickle을 사용하기 위해서는 바이너리를 적어줘야 함
# pickle은 따로 인코딩 할 필요 없다.
pickle.dump(Any, file)
profile_file = open("profile.pickle", "wb")  # profile 라는 이름의 pickle 파일을 만든다.
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}  # profile 사전 형태 데이터
print(profile)
# profile 에 있는 데이터를 profile_file에 담겨있는 profile.pickle파일에 저장
pickle.dump(profile, profile_file)
profile_file.close()

print("--------------------")

# pickle.load(file) # pickle확장자인 file 안에 있는 내용을 데이터로 가지고 옴
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # 파일의 형태(내용)을 데이터로 profile에다 담아 가지고 옴
print(profile)
profile_file.close()
