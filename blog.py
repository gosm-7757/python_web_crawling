import requests
from bs4 import BeautifulSoup
# 이 프로그램은 네이버 블로그 게시글을 100개 가져오는 프로그램이다.

# 사용자에게 검색어를 입력받는다.
검색어 = input("검색어 입력 => ")

# 몇개의 게시글을 확인할 것인지 묻는다.
게시글수 = int(input("몇 개의 게시글이 필요한가요? => "))

# 30개의 단위로 보여주므로 조건문을 작성한다.
    # 처음부터 30개의 게시글만 가져온다. 
data1 = requests.get(f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={검색어}')
soup1 = BeautifulSoup(data1.text.replace('\\',''), 'html.parser')
글리스트1 = soup1.select('a.api_txt_lines') # 블로그의 제목만 가져오기
# 출력
for i in range(30):
    print('제목 : ', 글리스트1[i].text) # 블로그의 제목 글자만 가져오기
    print('url : ',  글리스트1[i]['href']) # 블로그의 url 가져오기

data2 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=31&query={검색어}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=06230112&fgn_region=&fgn_city=&lgl_lat=35.893749&lgl_long=128.61855&abt=&_callback=viewMoreContents')
soup2 = BeautifulSoup(data2.text.replace('\\',''), 'html.parser')
글리스트2 = soup2.select('a.api_txt_lines') # 블로그의 제목만 가져오기

for i in range(30):
    print('제목 : ', 글리스트2[i].text) # 블로그의 제목 글자만 가져오기
    print('url : ',  글리스트2[i]['href']) # 블로그의 url 가져오기
    
# 30개씩으로 고정해야 된다. 