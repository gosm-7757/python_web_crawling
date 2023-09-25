import pandas as pd

path = 'D:/python_web_crawling/pandas'
# 판다스로 엑셀 파일 열기
raw = pd.read_excel(path + '/product.xlsx', engine="openpyxl") #pip install openpyxl : 엑셀 해석 엔진


raw['부가세포함'] = raw['판매가'] * 1.1 # 새로운 컬럼을 만드려면
#print(raw)

# 10%를 더해주는 함수
def 함수(num) :
    return num * 1.1

# 컬럼을 쉽게 조작해주는 apply
raw['부가세10%'] = raw['판매가'].apply(함수) # 특정 컬럼에 있는 모든 데이터를 함수에 넣었다가 빼줘
# print(raw)


import re  # 정규식 : 글자를 검사하는 것 (어떤 단어가 들어가 있는지 regex)
re.search('abc', 'abcddf') # (이 글자가, 이 글자안에 들어가 있나) ^ 단어로 시작하냐

def 카테고리분류(product):
    if re.search("Chair", str(product)):
        return "의자"
    elif re.search("Table", str(product)):
        return "테이블"
    elif re.search("Sofa", str(product)):
        return "소파"
    else:
        return "거울"
    
# 새로운 컬럼을 만들거나 이미 존재하면 덮어씀
raw['카테고리'] = raw['상품목록'].apply(카테고리분류)
print(raw)

# 판다스의 데이터는 전부 다 오브젝트형이다.


# 상품 목록에 MIRROR 또는 SOFA라는 영단어가 포함되어 있으면 카테고리 컬럼에 "가구"라고 기록하고 싶다.
def 함수스(a):
    if re.search('Mirror|Sofa', str(a)):
        return "가구"
    
raw['카테고리'] = raw['상품목록'].apply(함수스)


# 상품목록에 글자가 없고 숫자만 있으면 그 칸은 "에러"라는 단어로 바꾼다.
def 에러(a):
    if re.search("\D", str(a)) :
        return "에러"
    else:
        return a
    
raw['상품목록'] = raw['상품목록'].apply(에러)