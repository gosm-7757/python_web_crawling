# 이미지 100만개를 한번에 리사이즈하고 용량을 압출하려면
# 특히 파이썬으로 웹 서버를 만들 때 이미지 압축이 필요
# pip install Pillow 파이썬 이미지 라이브러리
from PIL import Image
img_jpg = Image.open('learning_crawling/images_zip/images/photo1.jpg').convert('L') # 흑백 변환
# img_jpg.resize((300, 500))  # 가로, 세로 (이미지가 짜부될 수 있음)
# img_jpg.thumbnail((300,500)) # 가로, 세로 (이미지 비율을 유지하면서 리사이즈) 가상의 박스 안에 맞춤
img_croped = img_jpg.crop((50, 50, 150, 150)) # 이미지 자르기 (좌표) (왼쪽 위 좌표, 오른쪽 아래 좌표 )

img_jpg.save('learning_crawling/images_zip/images/new_photo1.jpg',quality=65, progressive=True) # 이미지를 저장 // progressive=True 웹상에서 더 빠른 로딩시간 제공
# jpg 파일의 용량을 압축하고 싶으면 quality 속성 사용 (0 ~ 95, 기본 75)

# png 파일의 용량을 압축하고 싶으면 quantize 사용 // 이미지 압축이 안됨 
# Image.quantize(colors=256, method=None, kmeans=0, palette=None, dither=1)

# png 파일을 jpg로 변환
img_png = Image.open('learning_crawling/images_zip/images/photo4.png')
img_png.thumbnail((300, 500))
img_png.save('learning_crawling/images_zip/images/new_photo4.jpg')

# 100만개 사이즈를 줄여보자
import os
경로 = os.getcwd() # 현재 작업 디렉터리의 절대 경로를 가져옴
print(경로)
# 파일들을 다 가져옴
파일들 = os.listdir(경로 + '/learning_crawling/images_zip/images')
print(파일들)

for i in 파일들 :
    img_zip = Image.open(f'learning_crawling/images_zip/images/{i}')
    img_zip.thumbnail((500, 2500))
    img_zip.save(f'learning_crawling/images_zip/images/roop_new_{i}')
