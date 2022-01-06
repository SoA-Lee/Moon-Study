# 2-1
# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들기

# 내 풀이
def min_cal(v):
  n = len(v)
  a = v[0]
  for i in range(1,n):
    if ( a > v[i] ):
      a = v[i]
  return a

v = [3, 8, 2, 11, 25, 19]
print(min_cal(v))

# 정답 풀이
def find_min(a):
  n = len(a)
  min_v = a[0]
  for i in range(1,n):
    if a[i] < min_v:
      min_v = a[i]
  return min_v

v = [3, 8, 2, 11, 25, 19]
print(find_min(v))

# 변수명 좀 더 신경 쓰기 
# 계산 복잡도 O(n)
