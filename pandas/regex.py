# 전처리 : 더러운 데이터를 필터링하는 것
# 정규식 : 문자를 검사하는 식 (a글자가 들어갔나, 특수기호가 있다 등등)
import re

#re.search("정규식", "안녕하세요 정규식") # 찾으면 오브젝트 자료형을 주고 없으면 none
a = re.findall("^정규식", "안녕하세요 정규식") # 리스트로 보기 좋게 해준다.  (^ 시작, $ 끝)
a = re.findall("\$", "awdsa$awd") # 특수기호를 찾으려면 백슬레시 필요
a = re.findall("[abc]", "awnsianvacavb") # a 또는 b 또는 c를 찾아주세요
a = re.findall("[abcdefghijklmnopqrstuvwxyz]", "AwnSianvDcavb") # 소문자를 찾아주세요
a = re.findall("[a-zA-Z]", "AwnSianvDcavb")  # 소대문자 전부 찾아주세요
a = re.findall("[가-힣]", "ㅁㅈㅇㅁㄴdkssu 안녕하세요") # 한글을 다 찾아주세요
a = re.findall("[ㄱ-ㅎ]", "여기서 아무거나 찾아주셈 zdadwㅁㅈㅇㅁㄴ")
a = re.findall("[0-9]", "a숫자가 존재하는가1234")
a = re.findall("\d\d", "두자리 숫자가 존재하는가1234") # 알잘딱하게 끊음
a = re.findall("\d{8}", "두자리 숫자가 존재하는가1234") # n개의 자리수의 숫자가 존재하는가 (곱하기) 
a = re.findall("[^0-9]", "a숫자가 아닌 것이 존재하는가")
a = re.findall("\D", "숫자가 아닌 것이 존재하는가1234") 
a = re.findall("\s", "스페이즈바인 것이 존재하는가1234")  # 스페이스바가 존재하는 가
a = re.findall("\S", "스페이스바가 아닌 것이 존재하는가1234") 
print(a)
a = re.findall("ㅋ+", "숫자가 아닌 것이 존재하는가ㅋㅋㅋㅋㅋ") # 이어지는 글자를 찾아줌
a = re.findall("abc", "Abc숫자가 아닌 것이 존재하는가1234", re.IGNORECASE) # 대소문자 구분없이 찾아준다. 

# 글자 변경
re.sub("이걸 찾아서", "이걸로 바꿔주셈", "문장")
b = re.sub("일본어", "한국어", "일본어는 어려워요")
b = re.sub("\-", ".", "2022-1-1") # 점으로 변경 
b = re.sub("\d", "", "hello안녕하세요 1234") # 숫자들을 공백으로 바꾸고 싶을 때
b = re.sub("\D", "", "hello안녕하세요 1234") # 숫자만 남기고 싶을 때
b = re.sub("[^\d]", "", "hello안녕하세요 1234") # 숫자만 남기고 싶을 때


# 이메일 형식이 맞는지 확인하는 정규식
result = re.findall("\S+@\S+\.\S+","abc@naver.com")
result = re.findall("[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]+","abc@naver.com")
print(result)




