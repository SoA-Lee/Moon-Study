# IpAddress 설정
import binascii
import ipaddress

ADDRESSES =[
'192.168.12.1',
]

for ipaddr in ADDRESSES :
    addr =ipaddress.ip_address(ipaddr)
    print(f'IP address: {addr!r}') #주소를 repr( )을 사용하여 강제 형변환
    print('IP version:',addr.version )
    print('Packed addr:',binascii.hexlify(addr.packed))
    print('Integer addr:',int(addr))
    print('Is private?:',addr.is_private )
    print() 

# IpAddress 설정2
import ipaddress

ADDRESSES = [
    '192.168.12.1/24',
]

for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip) # 인터페이스 주소
    print('{!r}'.format(iface))
    print('network:\n ', iface.network) # 네트워크 주소
    print('ip:\n ', iface.ip) # 호스트 주소
    print('IP with prefixlen:\n ', iface.with_prefixlen) # CIDR 표기
    print('netmask:\n ', iface.with_netmask) # 넷마스크
    print('hostmask:\n ', iface.with_hostmask) # 호스트마스크
    print( )