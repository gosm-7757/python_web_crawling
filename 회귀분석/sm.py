from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import statsmodels.api as sm

df = pd.read_table('./회귀분석/income.txt')
df = df.dropna() # nan값 지우기

def 함수(x, a, b, c) :
    return a * x + b* x ** 2 + c

opt, cov = curve_fit(함수, df['age'], df['income'])

x = np.array([1,2,3,4,5,6]) # 행렬에서 필요
plt.plot(x, 함수(x, opt[0], opt[1], opt[2]))
plt.show()


# --------------------------------
# statsmodels로 polynomial 분석하려면 
x = np.column_stack([df['age'], df['age'] ** 2, np.ones(79)]) # column_stack 각 항목을 하나씩 가져오는 함수 [요소1, 요소2, 1(상수)]
x = np.column_stack([df['age'], df['age'] ** 2])
y = df['income']
model = sm.OLS(y, x).fit() # 
print(model.summary())


# --------------------------------
# overfitting : 너무나도 정확할 때 (데이터 20개에 20차 함수 쓰는 격)
# 너무 많은 커브를 주는 것 보다 적절한 합의점을 찾을 것