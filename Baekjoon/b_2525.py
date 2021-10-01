a, b = map(int, input().split())
c = int(input())
sum = a * 60 + b
sum = sum + c
if sum >= 1440:
    sum -= 1440
print('%d %d' %(sum // 60, sum % 60))
