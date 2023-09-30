import numpy as np
import statsmodels.api as sm

키 = np.array([170, 180, 160, 165, 158, 176, 182, 172]).reshape((-1, 1))
몸무게 = np.array([75, 81, 59, 70, 55, 78, 84, 72])

# sm.OLS(y, x).fit() : y 결과, x 변수 
model = sm.OLS(몸무게, 키).fit()
#print(model.summary())

# Regression Result 해석
# R-squared (uncentered) : R값 (관계정도)
# Prob (F-statistic) : a가 0일 확률 (가설을 세우고 확률로 증명함)


# 변수 3개로 집값을 예측해보자
import pandas as pd
df = pd.read_csv('./회귀분석/california_housing.csv') # 캘리포니아 집값 데이터 가져오기
# print(df)

# 연식, 방 개수, 침실 개수로 집값을 예측해보자
# 집값 = year * ? + rooms * ? + bedrooms * ?  == ax1 + bx2 + cx3
model = sm.OLS(df['price'], df[['year', 'rooms', 'bedrooms']]).fit() # 2차원 데이터를 사용하면 여러 키 값을 가져올 수 있음
print(model.summary())

# 20년도에 지어진 방 1000개에 침실 200인 집값은 ?
a = model.predict([[20, 1000, 200], [30, 2000, 100]])
print(a)