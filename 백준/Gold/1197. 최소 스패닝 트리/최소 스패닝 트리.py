import sys
input = sys.stdin.readline
import heapq

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

heap = [[0,1]]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

result = 0
cnt = 0

while heap:
    if cnt == V:
        break
    c, b = heapq.heappop(heap)
    if visited[b] == 0:
        result += c
        visited[b] = 1
        cnt += 1
        for tmp in graph[b]:
            heapq.heappush(heap,tmp)

print(result)