import requests
import json
import time

# 이더리움 코인 url
url = [
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000",
]


# 수집해야할 url이 많을 경우 
def 함수(구멍):
    data = requests.get(구멍)
    data_dict = json.loads(data.content)
    return data_dict['data'][0]['Close']

""" 함수(url[0]) """

# 멀티 프로세싱 : 여러개의 파이썬 실행창 띄우기
# 멀티 스레딩 : cpu 병렬 처리 
# 병목현상 : 프로세스 하나가 변수 등을 사용중이라서 다른 프로세스들이 이용 못하고 기다리는 현상

# dummy가 없으면 스레딩, 있으면 프로세싱
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(4) # 사용할 프로세스의 개수를 넣어 줌
result = pool.map(함수, url)      # 동시 처리가 가능한 함수
pool.close()     # 나는 이제 그만 할랭
pool.join()       # 작업한 거 전부 가져와

print(result)




# map 함수 사용방법
# 리스트 내의 모든 요소에 똑같은 작업을 적용하고 싶을 때 사용
""" def 더하기(x):
    return x + 1

리스트 = [2, 3, 4, 5, 6] # 1씩 더려면

# 함수와 리스트를 받는다. (이 함수를 리스트에 적용해 줘)
결과 = map(더하기, 리스트) # 색이 바뀌면 내장 함수
print(list(결과)) # list()에 안 넣으면 그냥 주소값이 나옴 """
