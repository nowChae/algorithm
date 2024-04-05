from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

result_time = []
visited = [False]*100001

def bfs(n, k, time):
    queue = deque([n, time])
    visited[n] = True

    while queue:
        qn = queue.popleft()
        qt = queue.popleft()
        visited[qn] = True

        if qn == k:
            result_time.append(qt)
        
        if qn-1 >= 0 and not visited[qn-1]:
            queue.append(qn-1)
            queue.append(qt+1)
        if qn+1 <=100000 and not visited[qn+1]:
            queue.append(qn+1)
            queue.append(qt+1)
        if qn*2 <=100000 and not visited[qn*2]:
            queue.append(qn*2)
            queue.append(qt)

bfs(N, K, 0)
print(min(result_time))