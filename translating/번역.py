from papago import 번역기 # from 하위폴더명.파일명 import 함수명1, 함수명2, or *

# print(번역기('안녕'))

# 엑셀 파일 읽어오기
import pandas as pd 
data = pd.read_excel('translating/english-1.xlsx', engine='openpyxl')


# 내용이 많을때는 ittertuple() 사용해봐라
for i, j in data.iterrows() : # 열의 길이만큼 반복
    # print(i) # 행의 번호
    # print(j) # 행의 내용
    # print(j['english']) # 영어 문장만 뽑기 
    # print(번역기(j['english']))
    data.loc[i,  'korean'] = 번역기(j['english']) # 데이터프레임.loc([행, 열])
    
print(data)

# 파일 저장하기
data.to_excel('output.xlsx')
data.to_csv('ddd.csv')