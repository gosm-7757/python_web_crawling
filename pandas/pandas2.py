import pandas as pd

path = 'D:/python_web_crawling/pandas'
df = pd.read_csv(path + '/credit.csv')
print(df.head())

# correlation 값 구하기 (상관관계)
# 나이와 사용금액의 상관관계
print(df[['나이', '사용금액']].corr()) # 1과 가까울 수록 관계가 깊음

# 원하는 데이터만 걸러 보기 (필터링)
#print(df[df['나이'] >= 50]) # 50살 이상
#print(df.query("나이 >= 50 and 기혼 == 'Married'")) #나이 50 이상에 기혼자들만
print(df.query("나이 <= 50 and 성별 == 'M'")) # 50이하에 남자들만

# 기존 list 데이터를 dataframe을호 변환 가능 
셔츠 = [15, 20, 25] # 판매 개수
바지 = [150, 160, 170] # 판매 개수

딕셔너리 = { # 컬럼 이름 : 값들
    '셔츠판매량' : 셔츠,
    '바지판매량' : 바지
}
# 데이터 프레임으로 변환
df2 = pd.DataFrame(딕셔너리)
print(df2)


