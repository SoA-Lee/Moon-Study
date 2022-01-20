# 6-1
# 하노이탑 알고리즘

# 풀이
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # 원반 n-1개를 aux_pos로 이동
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반 to_pos로 이동
    print(from_pos, "->", to_pos)
    # aux_pos의 n-1개를 to_pos로 이동
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1,1,3,2)
print("n = 2")
hanoi(2,1,3,2)
print("n = 3")
hanoi(3,1,3,2)

# 재귀호출 이용
# 규칙 찾기, 그림으로 
