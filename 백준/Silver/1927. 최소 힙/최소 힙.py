import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
  i = int(input())

  if i == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, i)