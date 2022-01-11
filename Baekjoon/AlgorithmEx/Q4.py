# 4-1
# 1부터 n까지의 합 구하기를 재귀 호출로 구현하기

# 내 풀이
def sum(n):
    if (n <= 1):
        return 1
    return n + sum(n - 1)

print(sum(5))

# 정답 풀이
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n
print(sum(5))

# 4-2
# **다시 해보기**
# 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 구현하기

# 풀이
def find_max(a,n):
    if n == 1:
        return a[0]
    max = find_max(a, n-1)
    if max > a[n-1]:
        return max
    else:
        return a[n-1]

v = [1, 4, 11, 3, 5]
print(find_max(v, len(v)))

# 전체적인 구조 짜는 방법 익히기
# n개 자료 중 최댓값 구하고, n-1개 자료 중 최댓값과 n-1번 위치 값 중 더 큰 값 비교
