import requests
from bs4 import BeautifulSoup
# 검색어를 입력받아서 원하는만큼 게시글을 가져오는 프로그램

# 결과를 출력하는 함수 선언
def prtResult(naver, how_many, count):
    # 받아온 웹 사이트를 수프에 담갔다가 뺀다.
    soup_naver = BeautifulSoup(naver.text.replace('\\',''), 'html.parser')
    
    # 각 게시글을 특정하는 것들
    blogers = soup_naver.select('a.sub_txt') # 블로그 자체
    blogs = soup_naver.select('a.api_txt_lines') # 블로그 제목
    blogs_txt = soup_naver.select('a.total_dsc') # 블로그 내용

    # 가져온 게시글등에서 특정 정보를 하나씩 출력
    index = 0
    while True:
        print(f"{count + 1}\n블로그명 : {blogers[index].text}")
        print(f"게시글명 : {blogs[index].text}")
        print(f"내용 : {blogs_txt[index].text}")
        print(f"URL : {blogs[index]['href']}\n")
        count += 1 # 게시글의 수를 세어줌
        index += 1 # 다음 게시글의 내용을 위해 증가
        # 30개씩 보여주므로 index가 30이거나 index의 값이 how_many와 같으면 종료
        if index == 30 or index == how_many:
            how_many -= index
            return how_many, count
    

# 사용자에게 검색어를 입력받는다. 
search_title = input("검색어 입력 => ")
# 몇 개의 게시글을 볼 건지 입력받는다.
how_many = int(input("게시글 개수 입력 => "))

# 웹사이트 불러오기 
naver1 = requests.get(f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_title}')
naver2 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=31&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver3 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=61&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver4 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=91&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver5 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=121&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver = [naver1, naver2, naver3, naver4, naver5]


index = 0 # naver 리스트안에 있는 요소를 변경해 줄 인덱스
count = 0 # 게시글의 수를 세어 줄 변수
# 함수의 실행이 끝날 때마다 how_many의 값이 줄어든다.
while how_many != 0:
    how_many, count = prtResult(naver[index] , how_many, count)
    index +=1

        
