import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()
for i in range(1, N+1):
  queue.append(str(i))

result = []
count = 1
while queue:
  if count == K:
    r = queue.popleft()
    result.append(r)
    count = 1
  else:
    a = queue.popleft()
    queue.append(a)
    count+=1
  
print('<'+', '.join(result)+'>')