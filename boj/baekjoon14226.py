import sys
from collections import deque

input = sys.stdin.readline

S = int(input()) #만들고 싶은 수

visited = [[False]*1001 for _ in range(1001)]

def bfs():
    queue = deque([1,1,1]) #monitor, board, time
    visited[1] = True

    while queue:
        m = queue.popleft()
        b = queue.popleft()
        t = queue.popleft()

        if m == S:
            return t
        elif m < S:
            if m+b < 1001 and (not visited[m+b][b]):
                queue.append(m+b)
                queue.append(b)
                queue.append(t+1)
                visited[m+b] = True
            if b < m and 2*m < 1001:
                b = m
                queue.append(m)
                queue.append(b)
                queue.append(t+1)
        else:
            if (not visited[m-1]) and m-1 > 0: 
                queue.append(m-1)
                queue.append(b)
                queue.append(t+1)


print(bfs())

import sys
from collections import deque

input = sys.stdin.readline

S = int(input()) # 만들고 싶은 수

# visited 배열을 올바르게 초기화
visited = [[False] * 1001 for _ in range(1001)]

def bfs():
    queue = deque([(1, 0, 0)])  # (monitor, board, time)

    while queue:
        m, b, t = queue.popleft()

        if m == S:
            return t
        elif m < S:
            # Case 1: Paste from board to monitor
            if m + b < 1001 and not visited[m + b][b]:
                visited[m + b][b] = True
                queue.append((m + b, b, t + 1))
            # Case 2: Copy all from monitor to board
            if b < m and not visited[m][m]:
                visited[m][m] = True
                queue.append((m, m, t + 1))
        # Case 3: Delete one from monitor
        if m - 1 > 0 and not visited[m - 1][b]:
            visited[m - 1][b] = True
            queue.append((m - 1, b, t + 1))

    return -1  # If no valid sequence found

print(bfs())
