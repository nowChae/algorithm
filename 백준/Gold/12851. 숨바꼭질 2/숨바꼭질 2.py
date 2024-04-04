import sys
from collections import deque

input = sys.stdin.readline
visited = [False]*100001
N, K = map(int,input().split())

time_list = []

def bfs(n, k, time):
    queue = deque([n, time])
    min_time = -1
    while queue:
        dn = queue.popleft()
        dtime = queue.popleft()
        visited[dn] = True

        if dn == k:
            if min_time == -1:
                min_time = dtime
                time_list.append(dtime)
            else:
                if min_time < dtime:
                    return 
                else:
                    time_list.append(dtime)

        if dn-1 > -1 and not visited[dn-1]: 
            queue.append(dn-1)
            queue.append(dtime+1)
        if dn+1 < 100001 and not visited[dn+1]:
            queue.append(dn+1)
            queue.append(dtime+1)
        if dn*2 < 100001 and not visited[dn*2]:
            queue.append(dn*2)
            queue.append(dtime+1)     


bfs(N, K, 0)
print(time_list[0])
print(len(time_list))