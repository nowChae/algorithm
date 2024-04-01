#bfs

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
for i in range(K):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[a].sort()

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]

trash_count = []

def bfs(start_x, start_y, count):
    queue = deque([start_x, start_y])
    visited[start_x][start_y] = True

    while queue:
        x = queue.popleft()
        y = queue.popleft()

        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx == 0 or nx == N+1 or ny == 0 or ny == M+1 :
                continue
            else:
                if (not visited[nx][ny]) and (ny in graph[nx]):
                    visited[nx][ny] = True
                    queue.append(nx)
                    queue.append(ny)
                    count += 1

    return count

for i in range(1,N+1):
    for j in graph[i]:
        trash_count.append(bfs(i, j, 1))

print(max(trash_count))


