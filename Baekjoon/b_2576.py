import sys
input = sys.stdin.readline
nList = []
for i in range(7):
    a = int(input())
    if a%2 !=0:
        nList.append(a)
if nList:
    print(sum(nList))
    print(min(nList))
else:
    print(-1)
