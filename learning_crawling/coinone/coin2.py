import requests
from bs4 import BeautifulSoup
import json, time

# dummy가 없으면 스레딩, 있으면 프로세싱
from multiprocessing.dummy import Pool as Thread

# 각 url의 장 오픈 가격을 알려주는 함수
def prt_menu(url):
    result = []
    data = requests.get(url)
    data_dict = json.loads(data.content)
    open_time = time.strftime("%Y년 %m월 %d일  %H : %M", time.localtime(data_dict['body']['candles'][0]['dt']/1000))
    open_rate = data_dict['body']['candles'][0]['open'] + "원"
    close_time = time.strftime("%Y년 %m월 %d일  %H : %M", time.localtime(data_dict['body']['candles'][-1]['dt']/1000))
    close_rate = data_dict['body']['candles'][-1]['open']+ "원"
    result.extend([open_time, open_rate,close_time, close_rate])
    return result

def prt_result(url):
    data = requests.get(url)
    data_dict = json.loads(data.content)
    for i in range(len(data_dict['body']['candles'])):
        time_ = time.strftime("%Y년 %m월 %d일  %H:%M", time.localtime(data_dict['body']['candles'][i]['dt']/1000))
        open_ =  data_dict['body']['candles'][i]['open'] + "원"
        low_ =  data_dict['body']['candles'][i]['low']+ "원"
        high_ = data_dict['body']['candles'][i]['high'] + "원"
        close_ =  data_dict['body']['candles'][i]['close'] + "원"
        if i % 10 == 0 :
            print("\n")

        print(f"{i+1}\n시간 : {time_}")
        print(f"시작 가격 : {open_}")
        print(f"최저가 : {low_}")
        print(f"최고가 : {high_}")
        print(f"종가 : {close_}")
        
# 종목을 가져오는 코드
with open('D:/python_web_crawling/learning_crawling/coinone/codes.txt', 'r', encoding='UTF=8') as code_file:
    for i in code_file:
        print(i)
    print()
    
code = input("종목 입력 => ")
t = []

# 이더리움의 코인 url
url = [
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1687384800000&interval={'1H'}&1694582053341",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1688104800000&interval={'1H'}&1694582052562",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1688824800000&interval={'1H'}&1694582051863",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1689544800000&interval={'1H'}&1694582051322",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1690264800000&interval={'1H'}&1694582050066",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1690984800000&interval={'1H'}&1694582049612",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1691704800000&interval={'1H'}&1694582049091",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1692424800000&interval={'1H'}&1694582048712",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1693144800000&interval={'1H'}&1694582048204",
f"https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/{code}?lastDt=1693864800000&interval={'1H'}&1694582045646"
]


# 멀티 스레딩
# 멀티 프로세싱 : 여러개의 파이썬 실행창 띄우기
# 멀티 스레딩 : cpu 병렬 처리
# 병목현상 : 프로세스 하나가 변수 등을 사용중이라서 다른 프로세스들이 이용 못하고 기다리는 현상
pool = Thread(4)  # 사용할 프로세스의 개수를 넣어 줌
result = pool.map(prt_menu, url) # url 요소를 prt_open함수에 하나씩 적용
pool.close() # 나는 이제 그만 할랭
pool.join()   # 작업한 거 전부 가져와

# 그냥 result를 출력하려면 이렇게 해야된다.
# print(list(result))

# result에 담긴 내용을 하나씩 출력
for i in range(len(result)):
    print(f"{i+1}\n시작 날짜 : {result[i][0]}")
    print(f"시작 가격 : {result[i][1]}")
    print(f"종료 날짜 : {result[i][2]}")
    print(f"종료 가격 : {result[i][3]}\n")
    print()

choice = int(input("몇 일 데이터를 보시겠습니까? => "))
prt_result(url[choice-1])
