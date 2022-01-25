# 10-1
# 병합정렬 알고리즘1
# 풀이
def merge_sort1(a):
    n = len(a)
    if n <= 1 :
        return a
    mid = n // 2
    g1 = merge_sort1(a[:mid])
    g2 = merge_sort1(a[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort1(d1))

# 10-2
# 병합정렬 알고리즘2
# 풀이
def merge_sort2(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort2(g1)
    merge_sort2(g2)
    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort2(d2)
print(d2)
