# 11-1
# 퀵정렬 알고리즘1
# 풀이
def quick_sort1(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1] # 리스트의 마지막 값을 기준 값으로 설정
    g1 = []
    g2 = []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort1(g1) + [pivot] + quick_sort1(g2)

d1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort1(d1))

# 11-2
# 퀵정렬 알고리즘2
# 풀이
# 리스트 a에서 start에서 end까지 정렬할 것
def quick_sort_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 한 개 이하이면 정렬할 필요 없음
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀호출
    quick_sort_sub(a, start, i-1) # 기준 값보다 작은 그룹
    quick_sort_sub(a, i+1, end) # 기준 값보다 큰 그룹

def quick_sort2(a):
    quick_sort_sub(a, 0, len(a) - 1)

d2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort2(d2)
print(d2)

# 복잡도 O(n*logn)
