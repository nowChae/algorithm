from collections import deque
import sys

test = int(sys.stdin.readline())

for _ in range(test):
  N, K = map(int,sys.stdin.readline().split())
  importance = deque(list(map(int, sys.stdin.readline().split())))

  queue = deque([i for i in range(N)])

  count = 1
  while True:
    maxImportance = max(importance)
    if importance[0] == maxImportance:
      if queue[0] == K:
        print(count)
        break
      else:
        importance.popleft()
        queue.popleft()
        count += 1
    else:
      i = importance.popleft()
      q = queue.popleft()
      importance.append(i)
      queue.append(q)
      
