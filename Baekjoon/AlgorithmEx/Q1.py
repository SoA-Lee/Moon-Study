# 1-1
# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들기
# 예를 들어 n = 10 이라면 1^2 + 2^2 + 3^2 + ```` + 10^2 = 385

# 내 풀이
n = int(input())
s = 0
for i in range(1,n+1) :
    s = s + i*i
print(s)

# 정답 풀이
def sum_sq(n):
  s = 0
  for i in range(1, n+1):
    s = s + i * i
  return s
  
print(sum_sq((10)))
print(sum_sq((100)))
      
# 1-2
# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 공식은 (n * (n + 1) * (2n + 1)) / 6로 알려져있다.
# for 반복문 대신 해당 공식 사용하면 O(1)과 O(n) 중 무엇인가 
# 생각 : 사칙연산 횟수 총 6번, 하지만 n의 크기와 상관 없이 일정하므로 O(1) 해당 => 해당 방법이 더 빠르다.
