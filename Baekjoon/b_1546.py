N=int(input())
grade_list=list(map(int,input().split()))
max=max(grade_list)

new_list=[]
for i in grade_list:
    new_list.append(i/max*100)
average=sum(new_list)/N
print(average)
