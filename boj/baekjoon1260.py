#DFS - stack, 재귀 함수를 이용해 구현 - 갈 수 있는 점까지 - 깊이 우선 탐색
#BFS - queue를 이용해 구현 - 현재 정점이 연결된 가까운 점부터 - 너비 우선 탐색

from collections import deque

point, line, start = map(int,input().split())

#해당 인덱스 정점에 연결된 정점 정리 리스트 
graph = [[] for x in range(point + 1) ]

for _ in range(line):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#작은 정점 번호를 먼저 방문하기 위한 정렬
for g in graph:
  g.sort()

#DFS 정점 방문 상태 
visited_d = [False] * len(graph)

#DFS 함수 
def DFS(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)

#BFS 정점 방문 상태
visited_b = [False] * len(graph)
def BFS(graph, start, visited):
  queue = deque(start)

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
