# 소켓 연결 
import socket

host=input('hostname :')

try:
    name, aliases, addresses = socket.gethostbyname_ex(host)
    print(' Hostname :', name)
    print(' Aliases :', aliases)
    print(' Addresses :', addresses)
except socket.error as emsg:
    print('Error :', emsg)
    print( )

print()
    
hostip=input('ip address :')
hostname, aliases, addresses = socket.gethostbyaddr(hostip)
print('Hostname :', hostname)
print('Aliases :', aliases)
print('Addresses :', addresses)