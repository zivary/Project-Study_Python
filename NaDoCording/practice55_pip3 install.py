# pip3 install
# pip3 install --upgrade pip

# pip3 로 패키지 설치하기
# google 에서 pypi 검색
# https://pypi.org


# pip3 로 beautifulsoup4 설치하기
# pip3 install beautifulsoup4

# pip3 로 설치한 프로그램 리스트 보기
# pip3 list

# pip3 로 설치한 beautifulsoup4 의 상세정보 보기
# pip3 show beauifulsoup4

# pip3 로 설치한 beautifulsoup4 의 버전 upgrade 하기
# pip3 install --upgrade beautifulsoup4

# pip3 로 설치한 beautifulsoup4 삭제하기
# pip3 uninstall beautifulsoup4  


# beautifulsoup4 실행해보기
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())