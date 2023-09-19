# 단순 반복 웹업무 자동화하고 싶으면
# 구조가 어려운 사이트 크롤링 하고싶으면
# selenium을 사용하면 된다. 

# 1. 크롬 드라이버를 설치한다.
# 2. 내 크롬 버전과 맞는 드라이버를 설치한다. (아니면 낮은 버전으로) chrome://version 이렇게 하면 됨
# 3. pip install selenium을 설치한다. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # 브라우저 로딩 시간동안 기다리기 위함
from selenium.webdriver.common.by import By # 업데이트 때문에 많이 바뀐듯 
from selenium.webdriver.chrome.options import Options # 브라우저 닫힘 방지
import urllib.request

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# driver에 웹페이지의 모든 정보가 저장됨
driver = webdriver.Chrome(options=chrome_options) # 비워두면 꺼지더라
driver.get('https://instagram.com') # 내가 들어가고 싶은 웹 주소
driver.implicitly_wait(10) # 웹 브라우저 꺼짐 방지로 쓰려다가 요소 찾는데 시간 걸리는거 방지로 사용

# 자동 로그인
id_ = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
pw = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
id_.send_keys("gogosm7757") # 자동 입력 가능
pw.send_keys("dlatnals12")
pw.send_keys(Keys.ENTER) # 엔터키 눌러줘 라는 뜻
time.sleep(5)

# 페이지 이동
driver.get("https://www.instagram.com/explore/tags/사과/")
driver.implicitly_wait(10) # 요소가 안보이면 10초만 기다려봐라 (time.sleep() 대신)
# 첫째 사진 누름
# 여러개 선택될 경우 elements라고 적는다 (리스트로 저장해줌)
first_img = driver.find_element(By.CSS_SELECTOR, "._aagw")
first_img.click()


img_url = []
# 사진 저장
이미지 = driver.find_element(By.CSS_SELECTOR, "._aagu ._aagv img").get_attribute('src')
print(이미지)
img_url.append(이미지)
urllib.request.urlretrieve(img_url[0], 'D:/python_web_crawling/learning_crawling/instagram/사진저장/첫번째 사진.jpg')
time.sleep(2)
# 다음 버튼 누름
driver.find_element(By.CSS_SELECTOR, "._abl-").click()

이미지 = driver.find_element(By.CSS_SELECTOR, "._aagu ._aagv img").get_attribute('src')
print("\n" + 이미지)
img_url.append(이미지)
urllib.request.urlretrieve(img_url[1], 'D:/python_web_crawling/learning_crawling/instagram/사진저장/두번째 사진.jpg')
time.sleep(2)

if img_url[0] != img_url[1] : 
    print("성공")
# 다음 버튼 누름
driver.find_element(By.CSS_SELECTOR, "._abl-").click()






# 원하는 요소 클릭, 키 입력
""" driver.find_element(By.CSS_SELECTOR, "css 셀렉터").click()  # 클릭하기
driver.find_element(By.CSS_SELECTOR, "css 셀렉터").send_keys("입력 내용")
driver.find_element(By.CSS_SELECTOR, "css 셀렉터").send_keys(Keys.ENTER) # 엔터키 누르기 """

# 가끔 click()이 안될 때 강제 클릭하는 법
""" e = driver.find_element(By.CSS_SELECTOR,"css 셀렉터")
driver.execute_script('argument[0].click();', e) # 일단 외우자 """



# 해당 웹사이트의 내용을 뽑아오기
""" e = driver.find_element(By.CSS_SELECTOR, '#loginForm > a > span').text
a = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').text # name 속성으로 찾기
print(e)
print(a) """




""" By.ID	태그의 id값으로 추출
By.NAME	태그의 name값으로 추출
By.XPATH	태그의 경로로 추출
By.LINK_TEXT	링크 텍스트값으로 추출
By.PARTIAL_LINK_TEXT	링크 텍스트의 자식 텍스트 값을 추출
By.TAG_NAME	태그 이름으로 추출
By.CLASS_NAME	태그의 클래스명으로 추출
By.CSS_SELECTOR	css선택자로 추출 """