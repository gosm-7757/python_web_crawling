# 아마존 (종목코드 AMZN) 주식의 2020년 1월 1일부터 12월 31일 주식 가격을 YAHOO에서 가져와 20일, 60일 이동평균선을 그려라
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

df = data.DataReader('AMZN', 'yahoo', start='2020-01-01', end='2020-12-31')

df['rolling20'] = df['Close'].rolling(20).mean()
df['rolling60'] = df['Close'].rolling(60).mean()

plt.plot(df.index, df['rolling20'])
plt.plot(df.index, df['rolling60'])
plt.plot(df.index, df['Close'])

plt.show()


# 삼성전자와 LG전자의 매출 데이터를 이용하여 그래프로 그려라
import matplotlib.pyplot as plt

plt.plot([2018, 2019, 2020, 2021], [50000, 60000, 75000, 70000])
plt.plot([2018, 2019, 2020, 2021], [30000, 40000, 50000, 35000])
plt.xlabel("time")
plt.ylabel("slaes")
plt.legend(['samsung', 'LG'])
plt.show()



# 야후에서 2020년 비트코인 가격을 가져와 Close 가격을 그래프로 그리고 싶다.
# 근데 volume 항목이 2020년 평균 volume보다 높은 날의 가격만 그래프로 그리고 싶을 때 어떻게 해야하는가

# 데이터를 가져와서 volume 항목의 평균을 출력한다.
import pandas as pd 
from pandas_datareader import data

df = data.DataReader('BTC-USD', 'yahoo', start='2020-01-01', end='2020-12-31')
avg = df['Volume'].mean()
print(avg)

df['tf'] = df['Volume'] > avg
print(df)
a = df[df['tf'] == True]
print(a)

import matplotlib.pyplot as plt
plt.bar(a.index, a['Close'])
plt.show()