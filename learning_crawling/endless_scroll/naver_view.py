import requests
from bs4 import BeautifulSoup
import urllib.request

data = requests.get('https://finance.naver.com/item/main.naver?code=001570')
soup = BeautifulSoup(data.content, 'html.parser')

img = soup.select('#img_chart_area')[0]
print(img['src'])
urllib.request.urlretrieve(img['src'], 'D:/python_web_crawling/learning_crawling/endless_scroll/사진저장/바로저장')
