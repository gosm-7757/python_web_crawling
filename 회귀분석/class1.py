import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
# 키로 몸무게를 추정할 수 있을까?
키 = np.array([170, 180, 160, 165, 158, 176, 182, 172]).reshape((-1,1)) # 리스트를 2차원으로 만들어주는 함수
몸무게 = [75, 81, 59, 70, 55, 78, 84, 72]

# 키가 커질 수록 몸무게도 늘어나는 듯
plt.scatter(키, 몸무게)
#plt.show()

# OLS를 충족하는 선(Ordinary Least Squares 알고리즘)
# 중앙 직선과의 전체 오차를 구한 후 그 오차를 최소화 시키는 선이 OLS 충족선이다. 
# 총 오차를 구할 땐 각각의 오차들의 제곱값을 더한다. (음수가 발생할 수 있기 때문에)

# 아직 모르는 선은 수학식으로 표현 y = ax + b (a,b값을 찾으면 됨)

model = LinearRegression().fit(키, 몸무게) # 모델을 만들고 분석결과를 저장
print(model.score(키, 몸무게))      # r의 제곱값(0~1 사이의 값을 가짐) : 1에 가까울 수록 관계가 깊다라는 뜻
print(model.intercept_)                 # 오차를 줄일 수 있는 가장 좋은 b값
print(model.coef_)                        #  오차를 줄일 수 있는 가장 좋은 a값

# 좀 더 쉽게 예측하기
a = model.predict([[170], [180]]) # model.predict(x축 데이터) 
print(a)

# 회귀분석 선과 같이 보기
plt.scatter(키, 몸무게)
plt.plot(키, model.predict(키))
plt.show()

# 회귀 분석을 왜 쓰냐
# 두 데이터 간의 관계 파악에 사용
# OLS 알고리즘으로 선 그려서 파악
# 선이 있다면 예측도 가능 