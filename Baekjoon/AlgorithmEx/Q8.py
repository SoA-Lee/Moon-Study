# 8-1
# 선택정렬 알고리즘1
# 풀이

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(0, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while(a):
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d1 = [2, 4, 5, 1, 3]
print(sel_sort(d1))

# 8-2
# 선택정렬 알고리즘2
# 풀이
def sel_sort2(a):
    n = len(a)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

d2 = [2, 5, 4, 1, 3]
sel_sort2(d2)
print(d2)

# 복잡도 O(n^2)
