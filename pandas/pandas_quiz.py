import pandas as pd

path = 'D:/python_web_crawling/pandas'
df = pd.read_csv(path + '/credit.csv') 

# 남자이고 결혼한 사람은 싱글인 사람에 비해 사용금액이 높은가?
married_man = df.query("성별 == 'M' and 기혼 == 'Married'")['사용금액'].mean()
single_man = df.query("성별 == 'M' and 기혼 == 'Single'")['사용금액'].mean()
print("기혼자 사용금액 : ", int(married_man))
print("미혼자 사용금액 : ", int(single_man))
if married_man > single_man :
    print(f"기혼자가 {int(married_man - single_man)}$만큼 더 사용합니다.")
else:
    print(f"미혼자가 {int(single_man - married_man)}$만큼 더 사용합니다.")


# 연간 소득이 높을 수록 신용카드 사용금액이 높은가?
# 소득 항목은 문자열로 되어 있다.
print(df.groupby('소득')['사용금액'].mean()) # 소득에 따라서 얼마를 버는지 알 수 있다.
# corr로 상관관계를 통계내고 싶으면 소득을 문자열에서 숫자로 바꿔야 된다. 
