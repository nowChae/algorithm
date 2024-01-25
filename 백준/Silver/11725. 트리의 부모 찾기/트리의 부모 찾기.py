import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [False]*N
graph = [[] for _ in range(N)]
result = [0]*(N)
for _ in range(N-1):
  a, b = map(int,input().split())
  graph[a-1].append(b)
  graph[b-1].append(a)

def bfs(start,visited, graph):
  queue = deque([start])
  visited[start-1] = True
  while queue:
    v = queue.popleft()

    for i in graph[v-1]:
      if (not visited[i-1]):
        queue.append(i)
        visited[i-1] = True
        result[i-1] = v

bfs(1, visited, graph)
for i in range(1,N):
  print(result[i])