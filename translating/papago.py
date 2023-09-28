import os
import sys
import urllib.request
import json

def 번역기(문장):
    client_id = "Ji0jNyyN7Bf0vLLBo3KW" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "Fg84jUFKX5" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(문장)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        딕셔너리 = json.loads(response_body) # json을 딕셔너리로 변환
        번역된문장 = 딕셔너리['message']['result']['translatedText']
        return 번역된문장
        # print(response_body.decode('utf-8')) # json 데이터를 받는다 (문자 취급을 받음)
    else:
        print("Error Code:" + rescode)
        
