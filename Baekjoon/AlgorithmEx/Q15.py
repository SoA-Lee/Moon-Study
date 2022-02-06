# 15-1
# 친구 찾기 & 친밀도 계산 알고리즘
# 그래프
# 풀이
def print_all_freinds(g, start): # g: 친구 관계 그래프, start: 모든 친구를 찾을 자신
    qu = [] # 앞으로 처리해야할 사람
    done = set() # 큐에 저장한 사람 기록. 중복 방지

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0) # 사람이름, 친밀도
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin','Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_freinds(fr_info, 'Summer')
print()
print_all_freinds(fr_info,'Tom')
