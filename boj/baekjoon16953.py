#bfs

from collections import deque
import sys
input = sys.stdin.readline


A, B = map(int,input().split())

result = []
def bfs(start, end):
    queue_list = [start, 1]
    queue = deque(queue_list)

    while queue:
        s = queue.popleft()
        cnt = queue.popleft()
        if s == end:
            result.append(cnt)
        elif s < end:
            cnt += 1
            queue.append(s*2)
            queue.append(cnt)
            queue.append(s*10 + 1)
            queue.append(cnt)


bfs(A, B)
if len(result) == 0:
    print(-1)
else:
    print(min(result))
