weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "한파주의보":
    print("따뜻하게 입으세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("춘비물 필요 없어요.")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요. 나가지 마세요.")
elif  temp < 30 and temp >= 10:
    print("날씨가 좋아요. 놀러 나가세요.")
elif 10 > temp >= 0:
    print("외투를 챙기세요.")
else: 
    print("너무 추워요. 나가지 마세요.")
