# 16-1
# 미로 찾기
# 미로 정보 g, 출발 start, 도착 end
def getout_maze(g, start, end):
    qu =[]
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in g[v]:
            if x not in done: # 아직 큐에 추가되지 않은 꼭짓점
                qu.append(p+x)
                done.add(x)

    return "?"

maze = {
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b', 'd'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b', 'g', 'j'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j', 'o'],
    'l' : ['h', 'p'],
    'm' : ['i', 'n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}

print(getout_maze(maze, 'a', 'p'))
