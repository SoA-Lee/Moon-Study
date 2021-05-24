#try-except
'''
def menu( ) :
    print("0. normal")
    print("1. 0으로 나누기")
    print("2. 리스트 인덱스")
    print("3. 없는 파일 열기")
    print("4. 원하는 값 안주기")
    print("5. TypeError")
    
try:
    menu()
    n=int(input("Select your choice: "))
    if n==0:
        pass
    elif n==1:
        a=11
        b=0
        c=a/b
    elif n==2:
        a=[2,3,5]
        print(a[4])
    elif n == 3 :
        fp=open("abc.txt","r")
    elif n == 4 :
        int(input("Type abc :"))
    elif n == 5 :
        a="안녕"+3
        print(a)
        
except ZeroDivisionError :
     print('0으로 나누기 에러 발생')
except IndexError as e2 :
    print(e2)
except FileNotFoundError as e3 :
     print(e3)
except (ValueError, TypeError) as e4 :
    print(e4)
except :
    print("어떤 에러 발생")
else :
     print("에러 없음")
finally :
    print("예외처리 끝")
'''
# pickle
import pickle

data= {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
pickle.dump(data,open("data.pic","wb"))
data2=pickle.load(open("data.pic","rb"))

while True:
    ch=input("your data: ")
    try:
        print(data[ch.title()])
        data2[ch.title()]="new"
        pickle.dump(data2, open("data2.pic", "wb"))
        
    except:
        print("NO data")
        print(data)
        print(data2)
        break
    

















