# 5-1
# 최대 공약수 알고리즘

# 직관적인 최대공약수 알고리즘
def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i ==0 and b % i == 0:
            return i
        i = i - 1

# 유클리드- 재귀호출
def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b, a % b)

print(gcd(1,5))
print(gcd(24,32))

# 5-2
# 피보나치 수열 

# 풀이
def fibonacci(v):
    if v <= 1:
        return v
    return fibonacci(v-1) + fibonacci(v-2)

print(fibonacci(5))
print(fibonacci(7))

# 재귀호출 이용
# 어렵게 생각하지 말기, 단순하게 그림 그려보기
