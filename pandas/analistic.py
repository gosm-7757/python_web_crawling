import pandas as pd
from pandas_datareader import data #  pip install pandas_datareader

# 주식 데이터를 활용해본다.

#data.DataReader('종목코드', '가져올 사이트') # 주식 가격을 가져오는 함수
df = data.DataReader('AAPL', 'yahoo', start="2022-01-01", end="2023-01-01")
print(df)