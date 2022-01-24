# 9-1
# 삽입정렬 알고리즘1
# 풀이
def find_ins_idx(r,v) :
    for i in range(0,len(r)):
        if v < r[i] :
            return i
    return len(r)

def ins_sort1(a):
    result = []
    while(a):
        # 기존 리스트에서 한 개 꺼냄
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return  result

d1 = [2, 4, 5, 1, 3]
print(ins_sort1(d1))

# 9-2
# 삽입정렬 알고리즘2
# 풀이
def ins_sort2(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j >=0 and a[j] > key:
            a[j+1] = a[j] # 삽입할 공간 생기도록 한 칸 이동
            j -= 1
        a[j+1] = key

d2 = [2, 5, 4, 1, 3]
ins_sort2(d2)
print(d2)

# 복잡도 O(n^2)
