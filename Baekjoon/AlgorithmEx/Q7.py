# 7-1
# 순차 탐색
# 리스트에서 특정 숫자의 위치 전부 찾기

# 내 풀이
def search_list(a,x):
    n = len(a)
    result = []
    for i in range(0,n):
        if x == a[i]:
            result.append(i)

    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

# 7-2
# 학생 번호에 해당하는 학생 이름 찾기
# 내 풀이
def search_stu(x,no,name):
    n = len(no)
    for i in range(0,n):
        if x == no[i]:
            return name[i]

    return "?"

stu_no = [39, 14, 67, 105]
stu_name = ['Justin', 'John', 'Mike', 'Summer']

print(search_stu(67,stu_no,stu_name))
