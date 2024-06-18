def acc_days(i, j, visited, maps):
    stack = [(i, j)]
    rst = 0
    
    while stack:
        x, y = stack.pop()
        
        if x < 0 or y < 0 or x >= len(maps) or y >= len(maps[0]):
            continue
        
        if visited[x][y] or maps[x][y] == 'X':
            continue
        
        visited[x][y] = True
        rst += int(maps[x][y])

        stack.append((x, y+1))
        stack.append((x+1, y))
        stack.append((x, y-1))
        stack.append((x-1, y))
    
    return rst

def solution(maps):
    row = len(maps)
    column = len(maps[0])
    
    visited = [[False] * column for _ in range(row)]
    
    answer = []
    
    for i in range(row):
        for j in range(column):
            if maps[i][j] == 'X' or visited[i][j]:
                continue
            day = acc_days(i, j, visited, maps)
            if day != 0:
                answer.append(day)
    
    if not answer:
        return [-1]
    else:
        return sorted(answer)
