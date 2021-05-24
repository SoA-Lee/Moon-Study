# 동전던지기 게임

import random

money=50

print("동전 던지기 게임을 시작합니다.")

while money>0 and money<100:
    choice=random.randint(1,2)
    coin=random.randint(1,2)
    if choice==coin:
        print("맞췄습니다. $7을 얻습니다.")
        money=money+7
        print("현재 가지고 있는 돈:"+str(money)+"$")
    else:
        print("틀렸습니다. $10을 잃습니다.")
        money=money-10
        print("현재 가지고 있는 돈:"+str(money)+"$")
print("종료합니다.")
