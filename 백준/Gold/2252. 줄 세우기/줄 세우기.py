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

for i in range(1, N+1):
    if connect[i] == 0:
        queue.append(i)

while queue:
    r = queue.pop(0)
    print(r)

    for i in graph[r]:
        connect[i] -= 1
        if connect[i] == 0:
            queue.append(i)
            unvisited_count -= 1

    if unvisited_count == 0:
        break
