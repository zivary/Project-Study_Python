# list []

# 지하철 칸별로 10명, 20명, 30명

#  
print("--------------------")
subway = [10,20,30,20,30,40]
print(subway)
print("--------------------")
subway = ["유재석", "조세호", "박명수"]
print(subway)
print("--------------------")
# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))
print("--------------------")
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
print("--------------------")
# 정형돈씨를 유재석 / 조세호 사이에 태워 봄
subway.insert(1, "정형돈")
print(subway)
print("--------------------")
# 지하철에 있는 사람들 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print("--------------------")

# 정렬(sort)도 가능
num_list = [5,2,4,3,1,]
num_list.sort()
print(num_list)
# 역정렬도 가능
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)
print("--------------------")

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)
print("--------------------")

# 리스트 확장
num_list = [5,2,4,3,1,]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)
print("--------------------")
