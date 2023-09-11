import requests                             # 웹 페이지를 불러오기 위한 라이브러리
from bs4 import BeautifulSoup    # 불러온 웹 페이지를 이쁘게 보여주기 위한 라이브러리

# 주식 정보를 가져오는 함수
def 주식가져오기(주식코드):
    # 웹 사이트 가져오기
    site = requests.get(f'https://finance.naver.com/item/sise.naver?code={주식코드}') 
    # 가져온 웹 사이트를 html형식으로 보여주고 content로 뽑기 (그냥하면 결과 코드만 나옴)
    soup = BeautifulSoup(site.content, 'html.parser')
    # 내가 뽑아야 할 값들만 가져오기
    현재가 = soup.find_all('strong', id='_nowVal')[0].text
    상한가 = soup.select('#content > div.section.inner_sub > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(2) > span')[0].text
    하한가 = soup.select('#content > div.section.inner_sub > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(2) > span')[0].text
    # 결과 리스트에 결과를 저장하고
    result = [현재가, 상한가, 하한가]
    # 반환하기
    return result


# 사용자에게 보여줄 메뉴 함수
def 메뉴():
    # 계속 물어보기 위해 반복
    while True:
        with open('D:/파이썬 장인의 폴더/나혼자해보기/파일명.txt', 'r', encoding='UTF-8') as file_: 
            for i in file_:
                파일리스트.append(i.strip())
        with open('D:/파이썬 장인의 폴더/나혼자해보기/종목.txt', 'r', encoding='UTF-8') as file_:
            for i in file_:
                내용.append(i.strip().split(':'))
        for i in range(len(내용)):
            주식[내용[i][0]] = 내용[i][1]
        print("주식코드를 보려면 1번을 눌러주세요.")
        print("주식을 추가하려면 2번을 눌러주세요.")
        선택 = input("주식코드를 입력해주세요. => ")
        
        # 저장되어 있는 주식 종목 출력
        if int(선택) == 1:
            for key,value in 주식.items():
                print(f"{key}  \t{value}")
        
        # 새로 추가할 주식 종목을 위한 코드
        elif int(선택) == 2:
            # 키와 값을 입력받고
            키 = input("주식 이름을 입력해주세요. => ")
            값 = input("주식 코드를 입력해주세요. => ")
            # 파일을 열어서 추가하기
            with open('./종목.txt', 'a', encoding='UTF-8') as file_:
                file_.write("\n" + 키 + ":" + 값)
           
        # 코드 입력이 올바르지 않을 경우 재입력 요구        
        elif int(선택) > 2 and 1 > len(선택) > 6 :
            print("코드가 바르지 않습니다. 확인해주세요.")
            
        # 종목 코드가 올바르게 입력된 경우 반복을 끝냄
        else:
            결과 = 주식가져오기(선택)
            return 선택, 결과
    
    

def 결과출력(선택, 결과):
    주식이름 = [k for k, v in 주식.items() if v == 선택]
    print(f"{주식이름} 주식의 현재 상황")
    print(f"현재가 : {결과[0]}원")
    print(f"상한가 : {결과[1]}원")
    print(f"하한가 : {결과[2]}원") 
    저장 = input("저장하시겠습니까? [네/아니요]=> ")
    if 저장 == "네":
        while True:
            print("파일 목록을 보려면 1번을 입력하세요.")
            print("새로운 파일을 추가하려면 아무키나 눌러주세요.")
            어쩔래 = input("=> ")
            if 어쩔래 == '1':
                for i in range(len(파일리스트)):
                    print(파일리스트[i] + "\t")
            else:
                파일명 = input("파일명을 입력해주세요 => ")
                if 파일명 in 파일리스트:
                    파일 = open('./save/'+파일명, 'a', encoding='UTF-8')
                else:
                    파일 = open('./save/'+파일명, 'w', encoding='UTF-8')
                파일.write(f"{주식이름} 주식의 현재 상황\n현재가 : {결과[0]}원\n상한가 : {결과[1]}원\n하한가 : {결과[2]}원\n")
                파일.close()
                break
        
        
    
 
파일리스트 = []
내용 = []  
주식 = {} 

# 실행 구간
while True:
    선택, 결과 = 메뉴()
    결과출력(선택, 결과)
        
    계속 = input("끝내겠습니까? [네/아니요]=> ")
    if 계속 == '네':
        break
        