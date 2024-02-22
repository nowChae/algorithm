#프림 알고리즘
"""
step 0) 임의의 정점을 선택하여 비어있는 T에 포함시킨다. (이제 T는 노드가 한 개인 트리. )
step 1) T 에 있는 노드와 T 에 없는 노드 사이의 간선 중 가중치가 최소인 간선을 찾는다.
step 2) 찾은 간선이 연결하는 두 노드 중, T 에 없던 노드를 T에 포함시킨다. (step 1에서 찾은 간선도 같이 T에 포함됩니다.)
step 3)모든 노드가 T 에 포함될 때 까지, 1,2 를 반복한다.
"""
import sys
input = sys.stdin.readline
import heapq

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

heap = [[0,1]] # 가중치, 노드 (가중치 기준으로 힙을 정렬하기 위해)
 
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

result = 0
cnt = 0

while heap:
    if cnt == V: # 노드가 다 연결되면
        break
    c, b = heapq.heappop(heap) # 가중치 기준 정렬된 힙 pop
    if visited[b] == 0: #방문 안 한 노드라면(갈 수 있는 노드 중 가중치가 가장 작은 값임!) 
        result += c
        visited[b] = 1
        cnt += 1
        for tmp in graph[b]: # b와 연결된 모든 (가중치와 노드) 힙에 추가 
            heapq.heappush(heap,tmp)

print(result)