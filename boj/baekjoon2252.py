#시간 초과

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
connect = [0 for _ in range(N+1)]
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    connect[b] += 1
    graph[a].append(b)

state = [False] * (N+1)

queue = deque()
for i in range(1,N+1):
    if connect[i] == 0:
        queue.append(i)
        state[i] = True
        break

while queue or (sum(connect)!= 0):
    if queue:
        r = queue.popleft()
        print(r)
        for i in graph[r]:
            connect[i] -= 1
            if not state[i] and connect[i] == 0:
                queue.append(i)
                state[i] = True
    else:
        for i in range(1, N+1):
            if not state[i] and connect[i] == 0:
                queue.append(i)
                state[i] = True
                break
                
