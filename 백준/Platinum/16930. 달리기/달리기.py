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
        
        if x == x2-1 and y == y2-1:
            return dist[x][y]
        
        for i in range(4):
            for j in range(1, k + 1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if ground[nx][ny] == '#':
                    break
                if dist[nx][ny] != -1 and dist[nx][ny] <= dist[x][y]:
                    break
                if dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    
    return -1

print(bfs())
