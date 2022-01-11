# set (집합) : {}
# 중복이 안됨, 순서 없음
my_set = {1, 2, 3, 3, 2, 1, 1, 3, 2, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
print(java)
python = set(["유재석", "박명수"])
print(python)

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 를 할 수 있거나 python 을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)


