from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # 브라우저 닫힘 방지
import time
import pyperclip

# 네이버 로그인 뚫기
# 1. 복사 붙여넣기 이용 #? e.send_Keys('adwasad')

# 2. 실제 브라우저처럼 꾸미기 (내가 기존에 사용하던 크롬처럼 로그인 되있고 뭐 그런거...)
options = webdriver.ChromeOptions()  # 엄청 업데이트가 많이 되서 헷갈림
options.add_argument(r'user-data-dir=C:\Users\gmrdl\AppData\Local\Google\Chrome\User Data\Default')  # 크롬 계정 정보 가져오기
# chrome://version/ 크롬 버전 확인
# 거기에 있는 프로필 경로를 복사해오기 (r은 raw 데이터라는 뜻) 포맷팅될까봐

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # chrome_options는 사라짐
driver.get('https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fm.mail.naver.com%2F')

time.sleep(2)
# 이렇게 입력하면 입력 속도가 너무 빨라서 내가 봇인줄 앎
# pip install pyperclip 복사 붙여넣기 가능
pyperclip.copy('gogosm7757') # ctrl + c
driver.find_element(By.CSS_SELECTOR, '#id').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
pyperclip.copy('dlatnals12')
driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.CONTROL, 'v')
driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.ENTER)
