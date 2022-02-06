def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # 뒤에 end=" " 를 넣어주면 문장을 출력하고 줄을 바꾸지 않고 아래 문장을 이어서 출력함
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# 가변 인자
def profile(name, age, *language):
    # 뒤에 end=" " 를 넣어주면 문장을 출력하고 줄을 바꾸지 않고 아래 문장을 이어서 출력함
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
