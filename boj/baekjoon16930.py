#시간 초과
import sys
from collections import deque 
input = sys.stdin.readline

N, M, K = map(int,input().split())
visited = [[False]* (M) for _ in range(N)]

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

gym = []
for _ in range(N):
    gym.append(list(map(str, input().strip())))

start_x, start_y, end_x , end_y = map(int,input().split())

def bfs():
    queue = deque([start_x - 1, start_y - 1, 0])

    while queue:
        x = queue.popleft()
        y = queue.popleft()
        time = queue.popleft()

        visited[x][y] = True

        if x == end_x - 1  and y == end_y - 1:
            return time
        
        for j in range(4): # 방향
            for i in range(1, K+1): #최대 이동수

                nx = x + (i * dir_x[j])
                ny = y + (i * dir_y[j])
                nx_next = x + (i * dir_x[j]) + dir_x[j]
                ny_next = y + ( i * dir_y[j]) + dir_y[j]

                if  ( 0 <= nx < N ) and (0 <= ny < M):
                    if (not visited[nx][ny]) and (gym[nx][ny] == '.'):
                        queue.append(nx)
                        queue.append(ny)
                        queue.append(time+1)
                        if (0 <= nx_next < N) and ( 0 <= ny_next < M):
                            if gym[nx_next][ny_next] == '#':
                                break
                    elif (not visited[nx][ny]) and (gym[nx][ny] == '#'):
                        break
    return -1
print(bfs())


