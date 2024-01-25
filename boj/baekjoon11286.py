import sys
import heapq
input = sys.stdin.readline

N = int(input())
abs_heap = []

for _ in range(N):
  i = int(input())

  if i == 0:
    if len(abs_heap) == 0:
      print(0)
    else:
      print(heapq.heappop(abs_heap)[1])
  else:
    if i > 0:
      heapq.heappush(abs_heap, (i,i))
    else:
      heapq.heappush(abs_heap, (-i,i))
