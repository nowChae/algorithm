import sys
import heapq 

input = sys.stdin.readline

N = int(input())
max_heap = []

for _ in range(N):
  i = int(input())

  if i == 0:
    if len(max_heap) == 0:
      print(0)
    else:      
      print(heapq.heappop(max_heap)[1])  
  else:
    heapq.heappush(max_heap, (-i,i))


