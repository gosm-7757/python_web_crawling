import requests
from bs4 import BeautifulSoup
# 검색어를 입력받아서 원하는만큼 게시글을 가져오는 프로그램

# 사용자에게 검색어를 입력받는다. 
search_title = input("검색어 입력 => ")
# 몇 개의 게시글을 볼 건지 입력받는다.
how_many = int(input("게시글 개수 입력 => "))

naver1 = requests.get(f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_title}')
naver2 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=31&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver3 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=61&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver4 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=91&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
naver5 = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=121&query={search_title}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=04850310&fgn_region=&fgn_city=&lgl_lat=35.9561642&lgl_long=128.4910391&abt=&_callback=viewMoreContents')
 
def prtResult(naver, hou_many, count):
    soup_naver = BeautifulSoup(naver.text.replace('\\',''), 'html.parser')
    
    blogers = soup_naver.select('a.sub_txt') # 블로그 자체
    blogs = soup_naver.select('a.api_txt_lines') # 블로그 제목
    blogs_txt = soup_naver.select('a.total_dsc') # 블로그 내용

    while True:
        print(f"{count + 1}\n블로그명 : {blogers[count].text}")
        print(f"게시글명 : {blogs[count].text}")
        print(f"내용 : {blogs_txt[count].text}")
        print(f"URL : {blogs[count]['href']}\n")
        count += 1
        if count == 29 :
            how_many -= count
            return how_many
    
        
