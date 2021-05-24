import socket

addr=("127.0.0.1", 4444)

with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print("Server is started..")
    conn,addr=s.accept()    #요청 수락.(요청 오지 않을 경우 대기)
    print("client = {}:{}".format(addr[0],addr[1])) #정보 확인

    while(1): #반복
        data = conn.recv(1024) #데이터를 계속 받는다
        if data.decode() == "quit":
            print("quit connection")
            exit()
        conn.send(data)     #데이터 보내기
        print(int(data.decode()))  #출력
