
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = [False]*(100001) # 움직일 수 있는 최대 좌표
queue = deque([N, 0])
visited[N] = True
while True:
  cur = queue.popleft()
  sec = queue.popleft()

  if cur == K:
    print(sec)
    break
  else:
    if cur - 1 >= 0:
      if not visited[cur-1]:
        queue.append(cur-1)
        queue.append(sec+1)
        visited[cur-1] = True
    if cur + 1 <= 100000:
      if not visited[cur+1]:
        queue.append(cur+1)
        queue.append(sec+1)
        visited[cur+1] = True
    if cur * 2 <= 100000:  
      if not visited[cur*2]:
        queue.append(cur*2)
        queue.append(sec+1)
        visited[cur*2] = True
