# range
'''
def sum(n):
    hab=0
    for i in range(n,0,-1):
        if i==1:
            print(i,'= ',end='')
            hab=hab+i
        else:
            print(i,'+ ',end='')
            hab=hab+i
    return hab

num=int(input("input num : "))
print(sum(num))
'''
# 문자열 추가
list=[]
flag=1

text=input("Your message: ")

for i in range(len(text)):
    list.append(text[i])

for index, string in enumerate(list, start=1):
    if 'a' in string:
        print(index-1)
        flag=0
    if flag==1:
                print('a가 없습니다.')
                break
