# 크롤러를 만들었는데 시간이 오래걸리거나, 완료를 알려주거나 , 결과 파일을 전송해 주거나 할 때 이메일을 보내라고 하면 좋음
# 메일을 주고 받을 땐 smtp에 따라 주고 받음 (메일을 주고 받는 통신 프로토콜) simple mail transfer protocol
# 대부분의 메일 서비스 가입하면 smtp 서버를 원격으로 이용할 수 있는 권한을 제공 (내가 직접 smtp 서버를 만들지 않아도 된다. )

# 네이버 서버 빌려서 메일 전송하는 방법
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
# 메일 내용에 html 추가하는 법
msg = MIMEMultipart('alternative') # html 전송에 필요한 함수 
내용 = """
<h4>굵은제목</h4>
<button> 버튼 </button>
<img src="">
"""  # """은 안에서 엔터키를 자유롭게 칠 수 있다.
part1 = MIMEText(내용, "html")
msg.attach(part1)

# html 안쓸때
""" text = "메일 내용입니다" # 이메일 내용
msg = MIMEText(text)  """
 
msg['Subject'] ="이것은 메일제목" # 이메일 제목
msg['From'] = 'gogosm7757@naver.com' # 보내는 사람 이메일, 이름
msg['To'] = '고세구' # 받는 사람 이메일, 이름
print(msg.as_string())

                            # 네이버 smtp 서버 주소 (gmail도 가능)
s = smtplib.SMTP( 'smtp.naver.com' , 587 )  # 네이버 메일 환경설정에서 imap/smtp로 설정한다. (사용함 체크)
s.starttls() #TLS 보안 처리 (메일을 암호화해서 보내줭)
s.login( 'gogosm7757' , 'dlatnals12' ) #네이버로그인 (아이디, 비번)
s.sendmail( 'gogosm7757@naver.com', 'gmrdlswjfal12@naver.com', msg.as_string() ) #s.sendmail( '발송자이메일', '수신자이메일', msg.as_string() )
s.close()