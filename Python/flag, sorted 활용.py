# flag 활용

'''
d=[{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618','email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718','email':'lj@mail.com'}]

ans=''

while ans!='Q':
    print("N:name, P:phone, E:email, Q:quit)")
    ans=input("choose menu (first letter): ").upper()
    
    if ans=='N':
        s=input('search name: ')
        print('>>search list<<')
        flags=1
        for people in d:
            if s. title() in people['name']:
                print(people['name'], people['phone'], people['email'])
                flags=0
        if flags==1:
            print('does not exist.')
                        
    elif ans=='P':
         n=input('search phone number: ')
         print('>>search list<<')
         flagn=1
         for people in d:
            if n in people['phone']:
                print(people['name'], people['phone'], people['email'])
                flagn=0
         if flagn==1:
                print('does not exist.')
                         
    elif ans=='E':
         e=input('search email: ')
         print('>>search list<<')
         flage=1
         for people in d:
             if e in people['email']:
                  print(people['name'], people['phone'], people['email'])
                  flage=0
         if flage==1:
                print('does not exist.')
                
    elif ans=='Q':
        break
    
    else:
        print("Wrong menu! Please check menu.")
        continue
'''
# sotrted 활용
'''
import random

empty=set()
while len(empty)<6:
    r=random.randint(1,45)
    if r not in empty:
        empty.add(r)
    else:
        continue
print('pick list:',empty)
print('sorted list(DESC):',sorted(empty,reverse=True))
print('sorted list(ASC):',sorted(empty))
'''
# sorted 활용2

import random

empty=[]
while len(empty)<6:
    r=random.randint(1,45)
    if r not in empty:
        empty.append(r)
    else:
        continue
print('pick list:',empty)
empty.sort(reverse=True)
print('sorted list(DESC):',empty)
empty.sort()
print('sorted list(ASC):',empty)
