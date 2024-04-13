import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
space = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
queue = deque([])


idx = [-1, -1, -1, 0, 0, 1, 1, 1]
idy = [-1, 0, 1, -1, 1, -1, 0 ,1]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            queue.append((i, j, 0))
            space[i][j] = 0
            visited[i][j] = True

while queue:
    x, y, dist = queue.popleft()
    space[x][y] = dist
    
    for k in range(8):
        nx, ny = x + idx[k], y + idy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

line_max = []
for s in space:
    line_max.append(max(s))
print(max(line_max))

