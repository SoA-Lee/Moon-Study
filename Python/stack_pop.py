import sys #파이썬 내 인터프리터 제어

num=int(input())
cal=input()
nums=[0]*num

for i in range(num):
    nums[i]=int(input())

stack=[]

for j in cal:
    if 'A'<=j<='Z':
        stack.append(nums[ord(j)-ord('A')]) #ord():특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
                                            #append: 리스트의 맨 마지막에 추가한다.
    else:
        second=stack.pop()   #리스트이 맨 마지막 요소를 돌려주고 그 요소는 삭제한다. 
        first=stack.pop()
        if j=='+':
            stack.append(first+second)
        elif j=='-':
            stack.append(first-second)
        elif j=='/':
            stack.append(first/second)
        elif j=='*':
            stack.append(first*second)

print(f"{stack[0]:.2f}")
    



