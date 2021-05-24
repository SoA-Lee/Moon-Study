#클라이언트 작성-웹
import socket

with socket.socket() as s: #소켓 구현(소켓을 불러오는 것)
    addr=("www.daum.net",80) #주소 만들기(웹 통신에서는 443 or 80 사용)
    s.connect(addr) #통신 시작.
    s.send("GET /\n".encode()) #데이터 보내기
    data=s.recv(1024) #1024바이트 데이터 받
    print(data.decode())

#서버 작성-웹
import socket

with socket.socket()as s:
    addr=("0.0.0.0",80) #80번으로 개통하겠다.
    s.bind(addr)
    s.listen()
    print("start server..")

    #addr에는 클라이언트가 주소가 들어감.
    conn,addr=s.accept() #요청 수락.(요청이 오지 않으면 여기서 기다림)
    print("accept {}:{}".format(addr[0],addr[1]))
    data=conn.recv(1024)
    conn.send("Hi This is Web".encode())

#echo 클라이언트 작성
import socket
addr=("127.0.0.1",4444)
str1=input("echo: ").encode() #사용자에게 데이터를 받아서 바로 인코딩.

with socket.socket() as s:
    s.connect(addr) #연결해서 addr로 접속
    s.send(str1) #접속하고 데이터 바로 보내기
    data=s.recv(1024) #바로 데이터 다시 받기(똑같은 데이터)
print(data.decode())  #출력

#echo 서버 작성
import socket
addr=("0.0.0.0",4444)
with socket.socket()as s:
    s.bind(addr)
    s.listen()
    print("Server is started..")
    

