print("--------------------")
python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자로 출력
print(python.upper()) # 모든 문자 대문자로 출력
print(python[0].isupper()) # 0번째 문자가 대문자 인가? True
print(len(python)) # 문자열 python의 길이
print(python.replace("Python","Java")) # "python"을 "Java"로 변경
print("--------------------")
index = python.index("n") # "n" 처음 등장하는 지점
print(index)
print("--------------------")
index = python.index("n", index + 1) # "n" 두 번째로 등장하는 지점
print(index)
print("--------------------")
print(python.count("n")) # 문자열에 "n"이 몇번 등장하는지
print("--------------------")
print(python.find("Java")) # 문자열에 "Java" 를 찾아보고 없으면 -1을 반환
print ("h")
print("--------------------")
print(python.index("Java")) # "Java" 를 찾아보고 없다면 에러를 발생
print ("hi") # 윗줄의 에러로 실행X
print("--------------------")
