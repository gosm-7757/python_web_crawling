import requests
from bs4 import BeautifulSoup

# 아마존은 크롤링이 막혀있다.
#amazon = requests.get('https://www.amazon.com/s?k=%EB%AA%A8%EB%8B%88%ED%84%B0&crid=102YDWDKTXC8L&sprefix=%EB%AA%A8%EB%8B%88%2Caps%2C434&ref=nb_sb_noss_2')

# 아마존은 api를 사서 크롤링 해야된다. 
#print(amazon.status_code)  # 503 : 서버에서 연결을 차단함 
#print(amazon.content)

# 아마존 서버에서 내가 보낸 데이터의 헤더를 보고 접속 정보를 확인한다.
# 내 아이피 주소, 쿠키, 언어, 위치 등등 모든게 적혀있다.
# 헤더를 보고 내가 파이썬으로 자동으로 접속하려고 해서 막아버린 것이다. 

# 내 헤더 정보를 나도 보고 싶으면 네트워크 탭에 들어가서 https://www.amazon.com/s?k=%EB%AA%A8%EB%8B%88%ED%84%B0&crid=102YDWDKTXC8L&sprefix=%EB%AA%A8%EB%8B%88%2Caps%2C434&ref=nb_sb_noss_2
# 을 확인해보면 된다. 

# user agent에 파이썬을 통하였음 이라고 적혀있으면 막음 
# User-Agent: 내가 지금 어떤 os를 사용하는지 
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

# user agent를 변경하면 크롤링을 뚫을 수 있다. (키의 단어 첫 글자는 대문자로 적어야 적용이 잘 됨)
헤더스 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
쿠키 = {'aws-ubid-main' : '631-3527366-2640224',
      'aws-target-data' : '%7B%22support%22%3A%221%22%7D',
      'aws-target-visitor-id' : '1695300349945-40185.42_0',
      'regStatus' : 'registered',
      'noflush_locale' : 'ko',
      'AMCV_7742037254C95E840A4C98A6%40AdobeOrg' : '1585540135%7CMCIDTS%7C19622%7CMCMID%7C60008579929506250020721437789205779515%7CMCAAMLH-1695966395%7C11%7CMCAAMB-1695966395%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1695368795s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
      'aws-userInfo-signed' : 'eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImViYjdjODY1LTY3NGEtNDNjZi1hYzY2LTUxNGQ1YjQxNjlhYiJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiSEtuYnR3TFwvVzVaSXVLd09sU05HK3E2V1dLS0FOMjVzNmRcL004a01LeUxrPSIsImFybiI6ImFybjphd3M6aWFtOjo4NjAwNTU3OTgyODk6cm9vdCIsInVzZXJuYW1lIjoic3VtaW5pIn0.vENRBXjc95dxge0JaQwBmJe6gtbVftfXMb_9JJCLeggQpAodEmcFkr-cG7KL28VSFWvfrRMdNEK1KXYtAV1YJXKcoClwDRBpMZs6pNhKWY-MkwTXwu6kdvbb4dSkkXJl',
      'aws-userInfo' : '%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A860055798289%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22sumini%22%2C%22keybase%22%3A%22HKnbtwL%2FW5ZIuKwOlSNG%2Bq6WWKKAN25s6d%2FM8kMKyLk%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D',
      'noflush_awsccs_sid' : '08b22bdec91875a1057af39d367adbb57a5a53149aa8f0217d08199160fca001',
      'session-id' : '136-7082575-5541203',
      'session-id-time' : '2082787201l; i18n-prefs=USD',
      'sp-cdn' : 'L5Z9:KR',
      'skin' : 'noskin',
      'ubid-main' : '134-1956332-9890652',
      'session-token' : 'Wz5ZJQTxmFAkVxIZY+I2CYvBkPMOpL0GOR/WVGWadDPlc9ybjBomLKynGT/NYlHvcTrWKD7Df4OFPiop5mTC/njelA2Zzdv/mpXCGU7EhHi9LLHBFJLpsJfrrruOZV65NCP5T3K0CNSUPHv78syl8nUurYm9MfnDhq9hpxK7KwIIALesFeCFbdSsbpNrVGwFX9sp0JqMhuT9czgcBKzZeWyZFY6jSf6e/VWq5Xcg0597CK+4nPf8Jmw90H/0FN8tshr9CNB2+eUnOmR4v4c/1EC8lEwgoqpjabvriD37Q4jUSnKJg/LC17m0aDYwPc9uCKpYKPNhUguILhMYnpsIR0j1Rg5d8+KC',
      'csm-hit' : 'tb:RNS85JA9X8K84FFFK3FH+s-GKVD0NGRDN0576ZH52JC|1695439864587&t:1695439864587&adb:adblk_no'}

# 쿠키랑 user agent 정보를 넣어주면 뚫림
r = requests.get('https://www.amazon.com/s?k=%EB%AA%A8%EB%8B%88%ED%84%B0&crid=102YDWDKTXC8L&sprefix=%EB%AA%A8%EB%8B%88%2Caps%2C434&ref=nb_sb_noss_2', headers=헤더스, cookies=쿠키)
#print(r.content)
#print(r.status_code) 200

# 크롤링 뚫기 성공!
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.select('.a-size-base-plus')[0].text)
# 파이썬 크롤러를 막으려면 headers(user-agent)//200안옴 와 cookies//content안옴 를 이용하여 막으면 된다.


# 에러 처리 방법
""" if r.status_code == 200:
    print(soup.select('.a-size-base-plus')[0].text)
else:
    print("에러 발생") """
    
# 에러가 나서 코드가 멈추는 것을 예방하려면 
try:
    print(soup.select('.a-size-base-plus')[0].text)  # 이거 해보고
except:
    print("안되네여 ㅠ")    # 안되거나 에러뜨면 이거 해봐 