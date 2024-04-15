import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
ground = [input().strip() for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

def bfs():
    queue = deque([(x1-1, y1-1)])
    dist = [[-1] * m for _ in range(n)]
    dist[x1-1][y1-1] = 0
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == x2-1 and y == y2-1: #목적지 도착
            return dist[x][y] # 시간 리턴
        
        for i in range(4): # 방향
            for j in range(1, k + 1): # 최대 거리 
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 안이 아니면
                    break
                if ground[nx][ny] == '#':# 벽에 마주하면
                    break
                if dist[nx][ny] != -1 and dist[nx][ny] <= dist[x][y]: #이미 방문한 위치인데, 기록된 값이 현재와 같거나 작을 경우 더 탐색 X
                    break
                if dist[nx][ny] == -1: #아직 방문하지 않은 곳이면
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    
    return -1

print(bfs())
