import pandas as pd # pip install pandas (cmd 관리자 권한으로 다운받으면 됨)
# 데이터의 개수가 몇 만개 이상이 될 경우 엑셀 사용이 어려움
# pandas로 2차원 데이터를 쉽게 다룰 수 있음
import numpy as np

path = 'D:/python_web_crawling/pandas'
df = pd.read_csv(path + '/credit.csv') # pandas로 csv파일 여는 방법 (df = dataframe : 2차원 데이터, Series : 1차원 데이터 (리스트))
print(df.head()) # 위부터 5개의 항목만 출력 
#print(df) # 간단하게 간추려 출력 (맨 왼쪽에 나오는 숫자는 그냥 인덱스 번호이다.) 세로줄 제목을 컬럼이라고 부름

""" # 나이 평균을 구해보자
print(df['나이'].mean()) # 세로줄만 출력 (mean() 으로 평균을 구할 수 있음)
# 최빈값 출력
print(df['나이'].mode())
# 최대값 출력
print(df['나이'].max())
# 최소값 출력
print(df['나이'].min())

# 빠른 통계로 확인하고 싶다
print(df['나이'].describe()) # 각종 정보를 간추려서 출력해줌  """


# 카테고리에 따라 분석해보기
#df.groupby('성별').mean() # 성별에 따라서 데이터를 다시 정렬해줘
print(df.groupby('성별')['나이'].mean())
try :
    # 계속 오류남 (구글 코랩에서 가능한 듯)
    print(df.groupby('성별').mean())
except:
    print(df.groupby('성별')['나이'].median()) # 중앙값
