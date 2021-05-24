from ftplib import FTP

ftp=FTP("0.0.0.0") #ip주소 입력

print('banner: ',ftp.getwelcome()) #배너 확인
print('login: ',ftp.login()) #로그인
print('LIST: ',ftp.retrlines('LIST'))
print('RETR: ',ftp.retrbinary('RETR swlug.txt',
                              open('hello.txt','wb').write)) #파일 다운로드
print('STOR',ftp.storbinary('STOR swlug2.txt',
                            open('swlug2.txt','rb'))) #파일 업로드
