import socket

port=190
addr=("127.0.0.1",port) #DNS
socket.setdefaulttimeout(2)
#UDP
#소켓 오픈: 응답이 없음
#소켓 닫힘: 응답이 있음
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM)as s:
    #AF_INET:IPv4(어떤 영역에서 통신할 것인지),SOCK:UDP를 의미
    try:
        s.sendto("Data".encode(),addr) #데이터 전송
        s.recvfrom(1024)
        print("[+]{} udp port is opened".format(port))
    except Exception as e: #예외가 발생할 경우 'e'로 받음
        print(e)
        if str(e)=="timed out":
            #2초안에 응답이 안올 시에 나오는 문구, 소켓이 열려있는 경우나 방화벽이 활성화되어있는 경우
            print("[+]{} udp port is opened".format(port))
        else:
            print("[-]{} udp port is opened".format(port))
