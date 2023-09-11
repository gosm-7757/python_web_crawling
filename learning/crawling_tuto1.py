# pip는 라이브러리를 설치할 때 사용하는 코드 (다른 사람의 코드를 사용하고자 할 때)
import requests                             # 웹 사이트 접속을 도와주는 라이브러리
from bs4 import BeautifulSoup     # HTML 문서 분석을 도와주는 라이브러리

# 크롤링의 기본
# 1. 데이터가 들어있는 웹사이트에 접속 (html 문서 가져오기)
# 2. html 문서 속에서 필요한 정보만 뽑는다.

# 웹 사이트를 변수에 저장
web_site = requests.get('')
# print(web_site)                     # <Response [200]> 이라고 뜨면 정상
# print(web_site.content)        # html 문서 전체 내용을 확인 (정리되지 않음)
# print(web_site.status_code)  # 웹 페이지를 잘 가져오는지 상태코드로 확인

# html 문서를 읽기 좋게 변환
web_site_souped = BeautifulSoup(web_site.content, 'html.parser')
# print(web_site_souped)        # 일반적인 html 문서로 변환된다.

# 웹 크롤링 방법
# 1. 크롬으로 들어가서 개발자 도구 실행
# 2. 얻고자하는 데이터의 html 태그를 찾는다. (태그의 class, id를 확인)
# 3. 찾은 정보를 출력한다. 리스트형으로 출력되므로 index를 사용해서 원하는 부분만 출력한다.
#     =>          print(web_site_souped.find_all('태그이름', class_='클래스명')[index].text)
# 4. class에는 언더바를 추가해준다.
# 5. 태그 부분을 제거하고 글자만 보고 싶으면 text를 사용한다.
# print(web_site_souped.text)   # 전체 html의 글자 부분만 출력한다.
# print(web_site_souped.find_all('태그명', id='id명')[index].text)

var = web_site_souped.find_all('span', class_='tah')[2].text
print(var)


# case study
# 1. 글자가 해체되어 있는 경우에는 글자 상위 태그를 가져와서 index로 뽑는다.
# 안  녕  하  세  요 => 상위 태그를 찾고 index 0~4 까지 사용

# 2. class_나 id가 없고 태그만 있는 경우
# 상위 태그의 css 셀렉터 형식으로 찾기 (띄어쓰기는 하위태그를 의미 )
# print(web_site_souped.select('.클래스명 하위태그')[index].text)
# 태그와 셀렉터를 동시에 사용하여 찾기도 가능하다.
# web_site_souped.select('태그명#nah') # 띄어쓰면 하위에서 찾기때문에 무조건 붙여서 적는다.

# 3. 이미지 수집 방법
# img 태그에 적혀있는 src 주소를 가져오면 된다.
# img id='img_chart_area를 가져온다. (예)
img = web_site_souped.select('img#img_chart_area')[0]
# src 주소를 꺼낸다.
img_src = img['src'] # 딕셔너리형으로 되어 있다. 
# 가져온 이미지를 저장하려면 
import urllib.request
# 이미지를 가져와서 내가 지정한 파일명으로 저장해주는 코드

# 4. 여러 주식 정보를 동시에 가져오고 싶은 경우
# url의 변하는 부분을 확인한다. 












