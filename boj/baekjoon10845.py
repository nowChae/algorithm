from collections import deque
import sys

N = int(sys.stdin.readline())
command = []
for _ in range(N):
  command.append(tuple(sys.stdin.readline().split()))

queue = deque()
for c in command:
  if c[0] == "push":
    queue.append(c[1])
  elif c[0] == "pop":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.popleft())
  elif c[0] == "size":
    print(len(queue))
  elif c[0] == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif c[0] == "front":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif c[0] == "back":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])