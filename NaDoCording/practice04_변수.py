# 애완동물을 소개해 주세요~

from typing import DefaultDict


animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3

'''
이렇게 하면 여러 문장을 주석 처리 할 수 있습니다
'''

# 일괄적으로 주석을 처리 할 수 있습니다.
# 한번에 모두 주석 처리 할 수 있어요.

print("우리집 " + animal + "의 이름은 "+ name +"에요.")
hobby = "공놀이" 
# print(name+"는 " + str(age) +"살이며, " +hobby+"을 아주 좋아해요. ")
print(name,"는 ",str(age),"살이며, ",hobby,"을(를) 아주 좋아해요.")
#print(name+" 는 어른일까요? " + str(is_adult))
print(name,"는 어른일까요?",str(is_adult))



