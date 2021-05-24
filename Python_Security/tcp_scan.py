#tcp scan
import socket

with socket.socket()as s:
    addr=("127.0.0.1",9122) #1번째에는 IP주소, 2번째에는 포트번호
    try:
        s.connect(addr)
        print("9122 tcp socket is opened")
    except:
        print("9122 tcp socket is closed")
