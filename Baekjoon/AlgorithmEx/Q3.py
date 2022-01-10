# 3-1
# n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘

# 내 풀이
def match_two(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                result.add(a[i]+' - '+a[j])
    return result

name = ['Tom', 'Jerry', 'Mike']
print(match_two(name))

# 정답 풀이
def match_two(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
          print(a[i], "-", a[j])

name = ['Tom', 'Jerry', 'Mike']
print(match_two(name))

# O(n^2)
# 불필요한 검증 과정 삭제하기
