import requests
from bs4 import BeautifulSoup
import time

# 사용자에게 보여지는 메뉴
def prtmenu(read_file, append_file) :
    print("1번 종목확인    2번 종목추가    3번 종목상황출력")
    choice = input("메뉴선택 => ")
    if choice == '1':
        check_stock(read_file)
    elif choice == '2':
        add_stock(append_file)
    elif choice == '3':
        prt_stock_info(read_file)
    else:
        stop = input("나가시겠습니까? [네/아니요] =>")
        if stop == '네':
            return 'stop'
        elif stop != '아니요':
            print("잘못된 입력")
        
        

# 1번 선택시 실행 함수
def check_stock(file_ob1):
    for i in file_ob1: # 한 줄씩 출력
        item = i.strip().split(':') # 한 줄 당 리스트로 만들고 :를 기준으로 항목을 나눈다.
        result[item[0]] = item[1]
    for key, value in result.items() : 
        print(f"{key} : {value}")




# 2번 선택시 실행 함수
def add_stock(file_ob2):
    key = input("종목이름 입력 => ")
    value = input("종목코드 입력 => ")
    file_ob2.write(f'\n{key}:{value}')
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
        save_result(stock_name, result)
    elif save != '아니요':
        print("잘못된 입력")
    

def save_result(stock_name, result_ob) :
    with open('D:\python_web_crawling\learning_crawling\stock/save_stock_info.txt', 'a', encoding='UTF-8') as save_file:
        save_file.write(stock_name + "\n")
        for key, value in result_ob.items():
            save_file.write(f"{key} : {value}\n")
        print()
    




result = {}     # 결과를 담을 딕셔너리 
# 실행구간
read_file = open('D:/python_web_crawling/learning_crawling/stock/stock_items.txt', 'r', encoding='UTF-8')
append_file = open('D:/python_web_crawling/learning_crawling/stock/stock_items.txt', 'a', encoding='UTF-8')
while True:
    stop = prtmenu(read_file, append_file)
    if stop == "stop":
        break
    result.clear()
read_file.close()
append_file.close()
