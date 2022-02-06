def profile(name, age, main_lang):
    print(name, age, main_lang)


# 키워드 값을 같이 넣어주면 순서와 상관 없이 함수를 호출할 수 있다.
# 출력은 함수에 정의한 순서 그대로
profile(name="유재석", main_lang="파이썬", age=20)
profile(age=25, name="김태호", main_lang="자바")
