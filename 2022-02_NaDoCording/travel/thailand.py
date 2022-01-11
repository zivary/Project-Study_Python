class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박5일] 방콕, 파타야 여행 (야시장투어) 50만원")

if __name__ == "__main__":  # 이게 무슨 의미인지 모르겠다. # thailand.py에서 직접 이 구문을 실행한 경우
    print("Thailand 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Tailand 외이부에서 모듈 호출")