import requests
import json
import time # 시간 함수

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1668312000000&interval=1H&1694231196024')
#print(data.content) # json 데이터가 온다.
# 딕셔너리 {'자료이름' : '값'} 작은 따옴표
# json 자료형 {"자료이름" : "값"} 큰 따옴표
# 둘다 텍스트 취급을 받는다. 

딕셔너리 = json.loads(data.content) # json을 딕셔너리로 저장 
for i in range(200):
    dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['body']['candles'][i]['dt']/1000)) # 1000으로 나누어 뒤에 3자리 없애기
    print()
    print('시간 : ', dt)
    print('종가 : ',  딕셔너리['body']['candles'][i]['close'])
#    "dt": 1667592000000, epoch/unix 시간(1970년 1월 1일부터 몇초인지)(10자리 까지만 시간, 나머지 3개는 미리초 표시)

