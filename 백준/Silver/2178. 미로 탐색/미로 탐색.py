import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

def BFS(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 확인
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 벽
            if graph[nx][ny]==0:
                continue
            #이동 가능
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기
    return graph[N-1][M-1]

print(BFS(0,0))