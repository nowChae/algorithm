import sys
from collections import deque

def dfs(start, visited, graph, result): # 재귀
  visited[start] = True
  result.append(start)
  for i in range(len(visited)):
    if (not visited[i]) and (graph[start][i]):
      dfs(i, visited, graph, result)

def bfs(start, visited, graph,result): #큐
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    result.append(v)

    for i in range(len(visited)):
      if(not visited[i]) and (graph[v][i]):
        queue.append(i)
        visited[i] = True


computers = int(sys.stdin.readline())
connections = int(sys.stdin.readline())

graph = [[False]*computers for i in range(computers)]
visited = [False]*computers

for i in range(connections):
  a, b = map(int,sys.stdin.readline().split())
  graph[a-1][b-1] = True
  graph[b-1][a-1] = True

result = []

dfs(0,visited, graph, result)
print(len(result) - 1)