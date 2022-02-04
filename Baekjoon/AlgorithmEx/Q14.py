# 14-1
# 동명이인 찾기
# 딕셔너리
# 풀이
def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set() # 결과값 저장한 빈 집합
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

# O(n) // 딕셔너리 사용 안 할 경우, 이중 for문 O(n^2)

# 14-2
# 풀이
def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"

student_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(get_name(student_info, 105))
