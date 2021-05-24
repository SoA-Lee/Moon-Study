# 파이썬 자료구조1
'''
while True:
    sum=0
    str=" "
    s=input("숫자를 입력하시오:")
    if s=='':
        break
    
    for i in s:
        sum+=int(i)
        str=str+'+'+i
        
    str=str.replace('+','',1)
    print("입력받은 숫자:",s)
    print("각자리 숫자의 합:",end=" ")
    print(str,'=',sum)
'''
# 파이썬 자료구조2
'''
str=input("문자를 입력하시오: ")
repeat=" "
print("문자 수:",len(str))

for i in range(10):
    repeat+=str
    
print("10번 반복한 문자열:",repeat)
print("첫번째 문자:",str[0])
print("처음 3문자:",str[:3])
print("마지막 3문자:",str[-3:])

reverse=" "
count,i=0,0
count=len(str)

for i in range(0,count):
    reverse+=str[count-(i+1)]
    
print("문자 거꾸로:",reverse)

if str[7].isspace()==False:
    print("7번재 문자:", str[7])
else:
    print("7번째 문자가 없습니다.")

print("처음과 마지막 문자 제외한 문자열:",str[1:-1])
print("문자를 모두 대문자로 변경:",str.upper())
print("문자를 모두 소문자로 변경:",str.lower())
'''
 # 파이썬 자료구조3
name_list=[]
for i in range(3):
    s=input("이름 입력:").upper()
    name_list.append(s)
print(name_list)

while True:
    print("\ni(insert), a(append), s(sort), r(remove), q(quit)")
    print("희망하는 메뉴의 첫글자를 입력하세요.")
          
    ans=input("메뉴를 선택하세요:").lower()
    
    if ans=='i':
        num=" "
        while True:
            num=input("추가 위치(숫자):")
            if num.isdigit()==True:
                break
        add=input("삽입할 이름:").upper()
        num=int(num)
        name_list.insert(num-1,add)
        print(name_list)

    elif ans=='a':
        add=input("추가할 이름:").upper()
        name_list.append(add)
        print(name_list)
        
    elif ans=='s':
        print("명단:", end=" ")
        name_list.sort()
        print(name_list)
        
    elif ans=='r':
        rname=input("삭제할 이름:").upper()
        if rname in name_list:
            name_list.remove(rname)
            print(name_list)
        else:
            print("이름이 없습니다. 이름을 확인하세요.")
            print(name_list)
            continue
        
    elif ans=='q':
        print("최종명단:",name_list)
        break
    else:
        print("메뉴를 잘못 선택하셨습니다.")
        print(name_list)
        continue