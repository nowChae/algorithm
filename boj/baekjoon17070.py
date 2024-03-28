# 시간 초과
# memo를 이용하는 dp로 변경

import sys
input = sys.stdin.readline

N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int,input().split())))


#백트래킹? 
def pipe_connect(pipe, point_x, point_y, result):
    if point_x == N-1 and point_y == N-1:
        result += 1
        return result
    if pipe == 1: # 가로 모양 
        if point_y == N-1:
            return result
        elif point_x == N-1:
            if house[point_x][point_y+1] == 0:
                result = pipe_connect(1, point_x, point_y+1, result)
        else:
            if house[point_x][point_y+1] == 0:
                result = pipe_connect(1, point_x, point_y+1, result)
            if house[point_x][point_y+1] == 0 and house[point_x+1][point_y+1] == 0 and house[point_x+1][point_y] == 0:
                result = pipe_connect(2, point_x+1, point_y+1, result)
    elif pipe == 2: #대각선 모양
        if point_x == N-1:
            if house[point_x][point_y+1] == 0:
                result = pipe_connect(1, point_x, point_y+1, result)
        elif point_y == N-1:
            if house[point_x+1][point_y] == 0:
                result = pipe_connect(3, point_x+1,point_y, result)
        else:
            if house[point_x][point_y+1] == 0:
                result = pipe_connect(1, point_x, point_y+1, result)
            if house[point_x][point_y+1] == 0 and house[point_x+1][point_y+1] == 0 and house[point_x+1][point_y] == 0:
                result = pipe_connect(2, point_x+1, point_y+1, result)
            if house[point_x+1][point_y] == 0:
                result =  pipe_connect(3, point_x+1,point_y, result)
    else: #세로 모양
        if point_x == N-1:
            return result
        elif point_y == N-1:
            if house[point_x+1][point_y] == 0:
                result = pipe_connect(3, point_x+1,point_y, result)
        else:
            if house[point_x][point_y+1] == 0 and house[point_x+1][point_y+1] == 0 and house[point_x+1][point_y] == 0:
                result = pipe_connect(2, point_x+1, point_y+1, result)
            if house[point_x+1][point_y] == 0:
                result = pipe_connect(3, point_x+1,point_y, result)
    return result

print(pipe_connect(1,0,1,0))