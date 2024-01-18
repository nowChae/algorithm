# 메모리 초과 코드

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([N, 0])

while True:
  cur = queue.popleft()
  sec = queue.popleft()

  if cur == K:
    print(sec)
    break
  else:
    queue.append(cur-1)
    queue.append(sec+1)
    queue.append(cur+1)
    queue.append(sec+1)
    queue.append(cur*2)
    queue.append(sec+1)
