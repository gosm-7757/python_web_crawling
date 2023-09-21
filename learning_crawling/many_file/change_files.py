# 파일 조작 모듈
import os 

# 파이썬으로 pc 파일 조작

# 모든 파일을 가져와 줘
test = 'D:/python_web_crawling/learning_crawling/many_file/test'
files = os.listdir(test) # 역슬레시 2번
print(files) # 파일명을 리스트로 반환

# 파일명 변경
# os.rename(test + '\\txt1.txt', test + '\\1.txt')  # 내용들이 전부 다 영어로 되어있어야 됨


# 반복문으로 전부 변경
""" for i in range(len(files)):
    os.rename(test + f'\\{i+1}.txt', test + f'\\test{i+1}.txt') """
    
""" for i in os.listdir(test):
    os.rename(test + f'\\{i}', test + f'\\aa{i}') """
    
    
# 파일 복사
import shutil

for i in os.listdir(test) : 
    shutil.copy(f'test/{i}',  f'test2/{i}')