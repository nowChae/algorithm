from collections import deque
import sys

node, edge, start = map(int,sys.stdin.readline().split())

graph = [[False]*node for i in range(node)]

for i in range(edge):
  node1, node2 = map(int, sys.stdin.readline().split())
  graph[node1-1][node2-1] = True
  graph[node2-1][node1-1] = True

visited_d = [False]*node
visited_b = [False]*node


# 재귀를 이용해 구현
def dfs(start, visited, graph):
  visited[start-1] = True
  print(start, end=" ")

  for n in range(node):
    if (not visited[n]) and (graph[start-1][n]):
      dfs(n+1, visited, graph)

dfs(start, visited_d, graph)

# 큐를 이용해 구현
def bfs(start, visited, graph):
  queue = deque([start])
  visited[start-1] = True

  while queue:
    v = queue.popleft()
    print(v, end=" ")

    for n in range(node):
      if (not visited[n]) and (graph[v-1][n]):
        queue.append(n+1)
        visited[n] = True
    

print()
bfs(start, visited_b, graph)

