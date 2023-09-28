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
# -----------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# 선 그래프 그리는 법
# plt.plot([x축 데이터], [y축 데이터])
# plt.plot([1,2,3],[4,5,6])
# plt.show()

plt.plot(df.index, df['Close'], color='skyblue')
plt.xlabel('시간')
plt.ylabel('가격')
plt.legend(['애플']) # 범례 출력
plt.title("주식 정보")
plt.show()

# -----------------------------------------------------
# bar 차트 그리기
plt.bar([1,2,3], [4,5,6])
plt.show()

# -----------------------------------------------------
plt.pie([57,35,11], labels=['라면', '참치', '과자']) # 원형 파이 차트 
plt.show() 

# -----------------------------------------------------
plt.hist([160,165,170,152,175,170,156,170]) # 빈출 값을 구하는 차트
plt.show()

# -----------------------------------------------------
# 분포도 그리기
math = [1,23,5,13,2,42,21,23,12]
eng = [12,87,26,86,45,96,43,23,56]
plt.scatter(math, eng) 


# -----------------------------------------------------
# plt.stackplot(x축, y축, y축 ...) # 누적 그래프 그리기
plt.stackplot([1,2,3], [10,20,30], [30,20,50]) # y축에 같은 요소들끼리 합쳐서 보여줌
plt.show()


# -----------------------------------------------------
# 여러 요소를 한번에 그리고 싶으면
plt.plot([1,2,3], [10,20,30])
plt.plot([4,5,6],[10,20,30])
plt.show() # plot을 여러개 그리고 마지막에 show를 하면 됨


# -----------------------------------------------------
# 차트 크기 조절
plt.figure(figsize=(10,20))  # 가로 세로
plt.plot([1,2,3], [10,20,30])
plt.plot([4,5,6],[10,20,30])
plt.show()