import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [False]*N
graph = [[] for _ in range(N)]
result = [0]*(N)
for _ in range(N-1):
  a, b = map(int,input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

def bfs(start,visited, graph):
  queue = deque([start])
  visited[start-1] = True
  while queue:
    v = queue.popleft()

    for i in graph[v-1]:
      if (not visited[i]):
        queue.append(i+1)
        visited[i] = True
        result[i] = v

bfs(1, visited, graph)
for i in range(1,N):
  print(result[i])