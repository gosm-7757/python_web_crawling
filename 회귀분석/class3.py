from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import statsmodels.api as sm

# 탭으로 구분된 파일을 열 때
df = pd.read_table('./회귀분석/income.txt')
df = df.dropna() # nan값 지우기
# print(df) 

# 곡선 그래프가 나옴 => y = ax + bx^2 + c
plt.scatter(df['age'], df['income'])
# plt.show()

# 1차, 2차, 3차, 로그 함수 등등 
def 함수(x, a, b, c) :
    return a * x + b* x ** 2 + c

# 곡선을 그리는 메서드
# curve_fit(함수, x축 데이터, y축 데이터)
opt, cov = curve_fit(함수, df['age'], df['income']) # 데이터가 2개 도착함
# opt = abc값 , cov = 공분산
print(opt)

x = np.array([1,2,3,4,5,6]) # 행렬에서 필요
plt.plot(x, 함수(x, opt[0], opt[1], opt[2]))
plt.show()

