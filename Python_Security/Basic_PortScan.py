#! python
#PortScanPorgram

import socket

ip="172.30.1.31"
#portNums=[27,123,1900,9122,250]
portNums=list(range(1,46))

with open("portScanResult.txt",'w')as f:#결과를 저장할 파일 지정
    for portNum in portNums:
        try:
            with socket.socket() as s:
                s.settimeout(2)
                print("[+]try to connect to {}:{}".format(ip,portNum))
                s.connect((ip,portNum))
                s.send("Python Connect\n".encode())
                banner=s.recv(1024) #데이터를 받아서 banner변수에 넣어둠
                if banner:
                    f.write("[+]{} port is opened:{}\n".format(portNum,banner.decode()[:20]))
                else:
                    f.write("[+]{} port is opened:None\n".format(portNum))
                    
        except Exception as e:
            if str(e)=="timed out":
                f.write("[+]{} port is opened:{}\n".format(portNum,str(e)))
            else:
                print(e)

with open("portScanResult.txt",'r')as f:
    print("\n\n\n######## the result ########\n")
    print(f.read())
    print(">> the result in portScanResult.txt")
        
