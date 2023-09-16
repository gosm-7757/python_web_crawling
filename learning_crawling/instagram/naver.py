from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 네이버 웹 페이지 가져오기
driver = webdriver.Chrome(options=chrome_options) # 비워두면 꺼지더라
driver.get('https://www.naver.com')
time.sleep(2)

input_query = driver.find_element(By.CSS_SELECTOR,'input[name="query"]')
input_query.send_keys("사과")
input_query.send_keys(Keys.ENTER)
view = driver.find_element(By.CSS_SELECTOR,"#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(4) > a > i")
view.click()

