import pandas as pd
import pandas_datareader as pdr #  pip install pandas_datareader
from pandas_datareader import data
from datetime import datetime

print(pdr.__version__)

# 주식 데이터를 활용해본다.
start_date = datetime(2022,1,1)
end_date = datetime(2023,1,1)

#data.DataReader('종목코드', '가져올 사이트') # 주식 가격을 가져오는 함수
df = data.DataReader('AAPL', 'yahoo', start_date, end_date)
print(df)
print(df['Close'].plot()) # 최종가 출력 (컬럼하나(시리즈데이터)를 그래프로 보고 싶을 때 : 컬럼하나.plot())

# 삼성 전자
df2= data.DataReader('005930', 'naver', start_date, end_date)
print(df2['Close'].astype(float)) # dtype을 바꾼다.
print(df2.index)
# 데이터 프레임에는 인덱스 컬럼이 존재한다.

# 시계열 데이터 : 시간에 흐름에 따라 변하는 데이터
# 이동 평균선 : 일전 시간 간의 가격을 평균내서 그래프로 그린거
df2['rolling5'] = df2['Close'].rolling(5).mean() # 5일 이동평균선을 그리는 방법
df2['rolling5'].plot()
df2['Close'].plot()
df2['Close'].rolling(20).mean() # 20일 이동평균선을 그리는 방법