import requests
from bs4 import BeautifulSoup
import time
import urllib.request

# 사용자에게 보여지는 메뉴
def prtmenu(read_file) :
    print("1번 종목확인    2번 종목추가    3번 종목상황출력")
    choice = input("메뉴선택 => ")
    if choice == '1':
        check_stock(read_file)                      # 파일에 저장되어 있는 주식의 종류를 가져오는 함수 호출
    elif choice == '2':
        add_stock(read_file)    # 주식 종목을 추가하는 함수 호출
    elif choice == '3':
        prt_stock_info(read_file)                  # 주식 정보를 출력하는 함수 호출
    else:
        stop = input("나가시겠습니까? [네/아니요] =>")      # 1, 2, 3 이외의 입력인 경우 나가는지 물어본다.
        if stop == '네':                                # 나가는 경우 stop문자 반환
            return 'stop'               
        elif stop != '아니요':
            print("잘못된 입력")                    # 네, 아니요가 아닌 답변인 경우 무시하고 재실행
        
        

# 1번 선택시 실행 함수
def check_stock(file_ob1):
    for i in file_ob1: # 한 줄씩 출력
        item = i.strip().split(':') # 한 줄 당 리스트로 만들고 :를 기준으로 항목을 나눈다.
        if len(item) != 2:
            continue
        stock_dict[item[0]] = item[1]
    for key, value in stock_dict.items() : 
        print(f"{key} : {value}")




# 2번 선택시 실행 함수
def add_stock(read_file):
    key = input("종목이름 입력 => ")
    value = input("종목코드 입력 => ")
    with open('D:/python_web_crawling/learning_crawling/stock/stock_items.txt', 'a', encoding='UTF-8') as append_file:
        append_file.write(f'\n{key}:{value}')
    print("종목 입력 완료")




# 3번 선택시 실행 함수
def prt_stock_info(file_ob3):
    stock_code = input('주식코드를 입력해주세요 => ')
                                
    # 네이버에서 주식 정보를 가져올 것이다.
    naver_stock = requests.get(f'https://finance.naver.com/item/sise.naver?code={stock_code}')
    souped_stock = BeautifulSoup(naver_stock.content, 'html.parser')

    # 주식 정보 가져오기
    result['현재가'] = souped_stock.find_all('strong', class_='tah')[0].text
    result['거래량'] = souped_stock.find_all('span', class_='tah')[5].text
    result['상한가'] = souped_stock.select('#content > div.section.inner_sub > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(2) > span')[0].text
    result['하한가'] = souped_stock.select('#content > div.section.inner_sub > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(2) > span')[0].text

    # 결과 출력 코드
    for key, value in result.items() :
        print(f"{key} : {value}")
    save = input("저장하시겠습니까? [네/아니요] => ")
    if save == '네':
        stock_name = input("주식명 입력 => ")
        img = souped_stock.select('#img_chart_area')[0]['src']
        save_result(stock_name, img, result)  # 저장 함수 호출
        print("저장 완료")
    elif save != '아니요':
        print("잘못된 입력")
    
    

# 주식의 상황을 저장하는 함수
def save_result(stock_name, img, result_ob) :
    with open('D:/python_web_crawling/learning_crawling/stock/save_stock_info.txt', 'a', encoding='UTF-8') as save_file:
        # 사진을 저장하는 코드
        urllib.request.urlretrieve(img, f'D:/python_web_crawling/learning_crawling/stock/사진저장/{stock_name}.png')
        # 저장 시간
        tm = time.strftime("%Y년 %m월 %d일  %H : %M") 
        save_file.write("----------\n주식명 : " + stock_name + "\n" + tm + "\n\n")
        for key, value in result_ob.items():
            save_file.write(f"{key} : {value}\n")
    
    



stock_dict = {} # 저장된 주식을 담아올 딕셔너리
result = {}        # 현재 상황을 담아올 딕셔너리


# 실행 구간
with open('D:/python_web_crawling/learning_crawling/stock/stock_items.txt', 'r', encoding='UTF-8') as read_file :
    while True:
        stop = prtmenu(read_file) # 기본적으로 메뉴를 출력하는 함수 호출
        if stop == "stop": # 반환값이 stop이면 반복 탈출
            # 반복문을 나가기 전에 열린 파일들은 닫고 탈출
            break



