#위상 정렬
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
connect = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    connect[b] += 1

unvisited_count = N

queue = []

# 들어오는 선이 없는 값들을 큐에 넣음
for i in range(1, N+1):
    if connect[i] == 0:
        queue.append(i)

while queue:
    r = queue.pop(0)
    print(r)

    for i in graph[r]:
        #연결된 선을 제거
        connect[i] -= 1
        #들어오는 선이 없는 경우에만 큐에 넣음
        if connect[i] == 0:
            queue.append(i)
            unvisited_count -= 1

    if unvisited_count == 0:
        break
