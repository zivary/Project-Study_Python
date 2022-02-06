#모듈 직접 실행
# __all__
# from random import * 사용해본적 있음

from travel import *  # error  # *을 사용하면 모든걸 가지고 온다는 의미지만 개발자가 공개범위를 설정해 줘야 한다. __init__.py 파일에서 공개범위 설정 
# trip_to_01 = vietnam.VietnamPackage()  #__init__.py 에 __all__ = ["vietnam"]를 넣어줌 (?? 이해 못 함)
trip_to_02 = thailand.ThailandPackage()  #__init__.py 에 __all__ = ["thailand"]를 넣어줌 (?? 이해 못 함)
# trip_to_01.detail()
trip_to_02.detail()
print("--------------------")