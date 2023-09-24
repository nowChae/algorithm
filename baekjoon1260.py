#DFS - stack, 재귀 함수를 이용해 구현 - 갈 수 있는 점까지 - 깊이 우선 탐색
#BFS - queue를 이용해 구현 - 현재 정점이 연결된 가까운 점부터 - 너비 우선 탐색

from collections import deque

point, line, start = map(int,input().split())

graph = [[] for x in range(point + 1) ]

for _ in range(line):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for g in graph:
  g.sort()

visited_d = [False] * len(graph)
def DFS(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)



visited_b = [False] * len(graph)
def BFS(graph, start, visited):
  queue = deque([start])

  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

        
DFS(graph, start, visited_d)
print()
BFS(graph, start, visited_b)
