
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = [0]*(100001) # 움직일 수 있는 최대 좌표 - 도착 시 시간 저장
queue = deque([N])

while queue:
  cur = queue.popleft()

  if cur == K:
    print(visited[cur])
    break

  for i in (cur-1, cur+1, cur*2):
    if 0 <= i and i <= 100000 and (not visited[i]):
      queue.append(i)
      visited[i] = visited[cur] + 1
