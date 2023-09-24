import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

text = "메일 내용입니다"
msg = MIMEMultipart()
msg['Subject'] ="이것은 메일제목"
msg['From'] = '보내는자이메일'
msg['To'] = '받는자이메일또는이름'
msg.attach(MIMEText(text))
print(msg.as_string())

#원하는 파일 rb로 오픈
with open('보낼파일경로', 'rb') as 파일:
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(파일.read())

#파일 base64 인코딩
encoders.encode_base64(part)                                                        #ex) file_name.xlsx
part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"')
msg.attach(part)

s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls()
s.login( '네이버아이디' , '비번' ) 
s.sendmail( '보내는사람', '받는사람', msg.as_string() ) 
s.close()