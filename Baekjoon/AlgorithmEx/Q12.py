# 12-1
# 이분 탐색 알고리즘
# 입력: 리스트 a, 찾는 값 x
# 풀이
def binary_search(a,x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

d = [1, 4, 9, 16, 25, 34, 49, 52, 76]
print(binary_search(d,34))
print(binary_search(d, 50))

# 복잡도 O(logn)

# 12-2
# 재귀호출을 활용한 이분 탐색 알고리즘
# 풀이
def binary_search_sub(a, x, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid+1, end)
    else:
        return binary_search_sub(a, x, start, mid-1)
    return -1

# 리스트 전체를 대상으로 재귀호출 함수 호출
def binary_search2(a,x):
    return binary_search_sub(a, x, 0, len(a)-1)

d = [1, 4, 9, 16, 25, 34, 49, 52, 76]
print(binary_search2(d,34))
print(binary_search2(d, 50))
