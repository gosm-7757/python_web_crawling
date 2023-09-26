import pandas as pd
import pandas_datareader as pdr #  pip install pandas_datareader
from datetime import datetime as dt

print(pdr.__version__)

# 주식 데이터를 활용해본다.

""" start_date = datetime(2022,1,1)
end_date = datetime(2023,1,1)
 """
#data.DataReader('종목코드', '가져올 사이트') # 주식 가격을 가져오는 함수
#df = pdr.DataReader('AAPL', 'yahoo', start_date, end_date)
#df = pdr.get_data_yahoo('AAPL', start_date, end_date)

#print(df)


import pandas_datareader.data as web

start = dt(2010, 1, 29)
end = dt.today()
df = web.DataReader('GOOG', 'yahoo-actions', start, end)
print(df)
